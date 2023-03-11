# rest_api_app/models.py

from django.db import models
from django_fsm import FSMIntegerField, transition

class File(models.Model):
    STATUS_CHOICES = (
        (0, 'Pending'),
        (1, 'Processing'),
        (2, 'Completed'),
        (3, 'Error'),
    )
    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    national_id = models.CharField(max_length=255)
    birth_date = models.DateField()
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField()
    finger_print_signature = models.CharField(max_length=255)
    status = FSMIntegerField(choices=STATUS_CHOICES, default=0)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.national_id})"

    STATUS_CHOICES = (
        (0, 'Pending'),
        (1, 'Processing'),
        (2, 'Completed'),
        (3, 'Error'),
    )
    
    # Fields omitted for brevity
    
    status = FSMIntegerField(choices=STATUS_CHOICES, default=0)
    
    @transition(field=status, source=0, target=1)
    def start_processing(self):
        pass
    
    @transition(field=status, source=1, target=2)
    def complete_processing(self):
        pass
    
    @transition(field=status, source=1, target=3)
    def error_processing(self):
        pass

