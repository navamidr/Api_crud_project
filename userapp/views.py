from rest_framework.decorators import api_view
from rest_framework.response import Response
from userapp.models import User,Person
from userapp.serializer import UserSerializer,LoginSerializer,RegisterSerializer,UsersSerializer,PersonSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from userapp.decorators import user_role
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView,GenericAPIView




# patch request using generic api view 

class RequetPatch(GenericAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def patch(self,request,id):
        data = request.data
        obj = Person.objects.get(id=id)
        serializer = PersonSerializer(obj,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)


# pagination 
class Pagenumber(PageNumberPagination):
    page_size= 2

class Pagination(ListAPIView):
    queryset=Person.objects.all()
    serializer_class = PersonSerializer
    pagination_class = Pagenumber


class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    lookup_field = 'user_id' 


    @action(detail=True, methods=['get'],url_path='details')
    @user_role

    def user_details(self,request,user_id=None):
        try:
            user = self.get_object()
            return Response({
                "user_id":user.user_id,
                "name":user.name,
                "role":user.role,
            })
        except Person.DoesNotExist:
            return Response({"error":"user not found"},status=404)



# jwt based authentication

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self,request):
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class Protecteduser(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        return Response({'message':'you are authenticated!'})

# token based authentication

class Register(APIView):
    def post(self,request):
        _data = request.data
        serializer = RegisterSerializer(data=_data)

        if not serializer.is_valid():
            return Response({'message':serializer.errors},status=status.HTTP_404_NOT_FOUND)
        serializer.save()
        return Response({'message':'user created'},status=status.HTTP_201_CREATED)
    

class Login(APIView):
    def post(self,request):
        _data = request.data
        serializer = LoginSerializer(data=_data)

        if not serializer.is_valid():
            return Response({'messages':serializer.errors},status=status.HTTP_404_NOT_FOUND)
        user = authenticate(username= serializer.data['username'],password=serializer.data['password'])
        if not user:
            return Response({'message':'invalid'},status=status.HTTP_401_UNAUTHORIZED)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'message':'login successfull', 'token':str(token)},status=status.HTTP_201_CREATED)

        

#crud operation using APIView

class Userlist(APIView):
    def get(self,request):
        objuser = User.objects.all()
        serializer = UserSerializer(objuser,many = True)
        return Response(serializer.data)
    
    
    def post(self,request):
        data=request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class Userdata(APIView):
    def get(self,request,id):
        obj = User.objects.get(id=id)
        serializer = UserSerializer(obj)
        return Response(serializer.data)
    
    def put(self,request,id):
        data = request.data
        obj = User.objects.get(id=id)
        serializer = UserSerializer(obj,data=data,partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        # return Response(serializer.errors)
    
    def patch(self,request,id):
        data = request.data
        obj= User.objects.get(id=id)
        serializer = UserSerializer(obj,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        # return Response(serializer.errors)

    def delete(self,request,id):
        data = request.data
        obj = User.objects.get(id=id)
        obj.delete()
        return Response({'user deleted'})


@api_view(['GET'])
def user(request):
    user_details = {
        'name':'neethu',
        'age': 25,
        'place' :'EKM',
        'job' : 'Teacher'

    }
    return Response(user_details)

