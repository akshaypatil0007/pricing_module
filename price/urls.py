from django.urls import path
from .views import UserList,UserDetails
urlpatterns = [
    path('user/', UserList.as_view()),
    path('user/<int:id>', UserDetails.as_view()),
]
