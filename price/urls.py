from django.urls import path
from .views import UserList,UserDetails,index
urlpatterns = [
    path('user/', UserList.as_view()),
    path('', index,name='index'),
    path('user/<int:id>', UserDetails.as_view()),
]
