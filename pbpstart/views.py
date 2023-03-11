from rest_framework import viewsets
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework import status, generics
from django_filters.rest_framework import DjangoFilterBackend

import datetime


from .models import File
from .serializers import FileSerializer

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    
    parser_classes = (FileUploadParser,)
    
    def create(self, request, *args, **kwargs):
        file_obj = request.FILES['file']
        
        # Open the file and read its contents
        file_content = file_obj.read().decode('utf-8')
        
        file_lines = file_content.split('\n')
        
        header = file_lines.pop(0)
        
        processed_data = []
        
        # Loop over the remaining lines and process each one
        for line in file_lines:
            fields = line.split(',')
            
            if len(fields) != 9:
                # The line is invalid, so skip it
                continue
            
            first_name, last_name, national_id, birth_date, address, country, phone_number, email, finger_print_signature = fields
            
            birth_date = datetime.datetime.strptime(birth_date, '%Y-%m-%d').date()
            
            data = {
                'first_name': first_name,
                'last_name': last_name,
                'national_id': national_id,
                'birth_date': birth_date,
                'address': address,
                'country': country,
                'phone_number': phone_number,
                'email': email,
                'finger_print_signature': finger_print_signature
            }
            
            # Add the dictionary to the list of processed data
            processed_data.append(data)
        
        # Your code for inserting the processed data into the database goes here
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class UserListView(generics.ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'first_name': ['exact', 'icontains'],
        'last_name': ['exact', 'icontains'],
        'birth_date': ['exact', 'gte', 'lte'],
        'phone_number': ['exact', 'icontains'],
        'email': ['exact', 'icontains'],
    }
    ordering_fields = ['first_name', 'last_name', 'birth_date', 'phone_number', 'email']

