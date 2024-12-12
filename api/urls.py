from django.urls import path,include
from userapp.views import user,Userlist,Userdata

urlpatterns = [
    path('user/',user, name='user'),
    # path('api/',include('api.urls'),),
    path('userlist/',Userlist.as_view(),name='userlist'),
    path('userdata/<int:id>/',Userdata.as_view(),name='userdata'),
]