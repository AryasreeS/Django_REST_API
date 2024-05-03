from rest_framework import serializers
#import model 
from .models import User

# To enable APIs to read data more easily, serializers transform complex Django models into JSON objects.For that, the first thing you have to do is to create a new file in the serializer.py app.
class Userserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('name','email')
        
        
        
        
        