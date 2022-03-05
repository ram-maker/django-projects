from rest_framework import serializers
from .models import Student
class StudentSerializer(serializers.Serializer):
 name=serializers.CharField(max_length=50)
 roll=serializers.IntegerField()
 city=serializers.CharField(max_length=50)
 def create(self,validated_data):
     return Student.objects.create(**validated_data)
 def update(self, instance, validated_data):
     instance.name=validated_data.get('name',instance.name)
     instance.roll=validated_data.get('roll',instance.roll)
     instance.city=validated_data.get('city',instance.city)
     instance.save()
     return instance
#  def validate_roll(self,value): #validation for individual field
#      if value>=200:
#          raise serializers.ValidationError("Roll exceeded total student number")
#      return value
#  def validate(self,data): #object level vaidation
#      nm=data.get("name")
#      if nm.lower()!="ram":
#          raise serializers.ValidationError("name must be ram")
#      return data
   
