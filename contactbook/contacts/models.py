from django.db import models
from django.contrib.auth.models import User
import uuid

class Contact(models.Model):
    # Use UUID for better security (optional)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts')
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'email')  # Prevent same email under the same user
        ordering = ['-updated_at']

    def __str__(self):
        return f"{self.name} ({self.email})"
