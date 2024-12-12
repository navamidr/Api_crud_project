from rest_framework.decorators import api_view
from rest_framework.response import Response
from userapp.models import User
from userapp.serializer import UserSerializer
from rest_framework import status
from rest_framework.views import APIView

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

    # def post(self,request):


    


@api_view(['GET'])
def user(request):
    user_details = {
        'name':'neethu',
        'age': 25,
        'place' :'EKM',
        'job' : 'Teacher'

    }
    return Response(user_details)

