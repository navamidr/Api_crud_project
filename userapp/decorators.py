from functools import wraps
from rest_framework.response import Response
from rest_framework import status
from .models import Person

def user_role(func):
    @wraps(func)
    def wrapper(view_instance,request,*args,**kwargs):
        user_id = kwargs.get('user_id')
        user = Person.objects.get(user_id=user_id)
           
        if user and user.role != 'EMPLOYEE':
            return Response({"error": "Access denied: Not an employee"}, status=status.HTTP_403_FORBIDDEN)
        
        return func(view_instance, request, *args, **kwargs)
    return wrapper




