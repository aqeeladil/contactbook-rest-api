from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            'id',         # UUID
            'name',
            'email',
            'phone',
            'address',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_email(self, value):
        """
        Prevent duplicate email per user when creating a new contact.
        """
        user = self.context['request'].user
        if self.instance is None:  # Only validate on create
            if Contact.objects.filter(user=user, email=value).exists():
                raise serializers.ValidationError("You already have a contact with this email.")
        return value
