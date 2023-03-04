
# Now we make an complete CRUD operation using the serialization using the function in views.py
# I am using Django REST framework provides a set of already mixed-in generic views that we can use to trim down our views.py module even more

from .serializers import userSerializer
from.models import Price_Calculate
from rest_framework import generics

#for get the list of the user
class UserList(generics.ListCreateAPIView):
    queryset = Price_Calculate.objects.all()
    serializer_class = userSerializer

#to make modification and deletion of the user
class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Price_Calculate.objects.all()
    serializer_class = userSerializer
    lookup_field = 'id'


