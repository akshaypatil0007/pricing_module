
# Now we make an complete CRUD operation using the serialization using the function in views.py
# I am using Django REST framework provides a set of already mixed-in generic views that we can use to trim down our views.py module even more

from .serializers import userSerializer
from.models import Price_Calculate
from rest_framework import generics
from .tasks import send_email_task
from django.shortcuts import render,HttpResponse
#for get the list of the user
class UserList(generics.ListCreateAPIView):
    queryset = Price_Calculate.objects.all()
    serializer_class = userSerializer

#to make modification and deletion of the user
class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Price_Calculate.objects.all()
    serializer_class = userSerializer
    lookup_field = 'id'



#We are calling index function to send the mail by us.
def index(request):
  send_email_task()
  return HttpResponse('<h1>EMAIL HAS BEEN SENT WITH CELERY!</h1>')

