from rest_framework import serializers
from userapp.models import User,Person
from django.contrib.auth.models import User




class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


# jwt
class UsersSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)


    class Meta:
        model = User
        fields = ['id','username','password','email']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        return user

# token based

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()


    def validate(self,data):
        if data['username']:
            if User.objects.filter(username = data['username']).exists():
                raise serializers.ValidationError("username already exists")
        if data['email']:
            if User.objects.filter(email = data['email']).exists():
                raise serializers.ValidationError("email already exists")
                
        return data
        
    def create(self, validated_data):
        obj = User.objects.create(username = validated_data['username'], email= validated_data['email'])
        obj.set_password(validated_data['password'])
        obj.save()
        return validated_data
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'