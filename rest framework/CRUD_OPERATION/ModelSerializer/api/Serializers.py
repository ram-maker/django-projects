from rest_framework import serializers, validators
from rest_framework.fields import ReadOnlyField
from .models import Student
#validators
def start_with_r(value):
    if value[0].lower()!='r':
        raise serializers.ValidationError("Name must start with r")

class StudentSerializer(serializers.ModelSerializer):#Implementing model serializer
    #  name=serializers.CharField(read_only=True) #for individual property
    name=serializers.CharField(validators=[start_with_r])
    class Meta: 
        model=Student
        fields=['roll','name','city','id']
        # read_only_fields=['roll','name']
    #field level validation
    # def validate_roll(self,value): 
    #     if value>=200:
    #      raise serializers.ValidationError("Roll exceeded total student number")
    #     return value
    # object level vaidation
    # def validate(self,data): 
    #     nm=data.get("name")
    #     if nm.lower()!="ram":
    #      raise serializers.ValidationError("name must be ram")
    #     return data