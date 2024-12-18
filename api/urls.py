from django.urls import path,include
from userapp.views import user,Userlist,Userdata,Register,Login,RegisterView,Protecteduser,PersonViewSet
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'persons', PersonViewSet)

urlpatterns = [
    path('user/',user, name='user'),
    # path('api/',include('api.urls'),),
    path('userlist/',Userlist.as_view(),name='userlist'),
    path('userdata/<int:id>/',Userdata.as_view(),name='userdata'),
    path('register/',Register.as_view(),name='register'),
    path('login/',Login.as_view(),name='login'),
    path('registerview/',RegisterView.as_view(),name='registerview'),
    path('token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('token/refresh/',TokenRefreshView.as_view(),name='token_refresh'),
    path('protecteduser/',Protecteduser.as_view(),name='protecteduser'),

    
    path('', include(router.urls)),
    

 ] + router.urls