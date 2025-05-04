from rest_framework import viewsets, permissions, status
from .models import Contact
from .serializers import ContactSerializer
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class ContactViewSet(viewsets.ModelViewSet):
    """
    A viewset for authenticated users to manage their personal contacts.
    """
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['name', 'email']
    search_fields = ['name', 'email']


    def get_queryset(self):
        # Ensure users can only access their own contacts
        return Contact.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically associate the contact with the current user
        serializer.save(user=self.request.user)


