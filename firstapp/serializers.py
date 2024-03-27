from rest_framework import serializers
# from .models import ServicesApi
from services.models import Services
from django.core.exceptions import ValidationError
# class ServicesApiSirealizer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField()
#     description = serializers.CharField(max_length=None)
#     link = serializers.CharField()

#     def create(self, validated_data):
#         return ServicesApi.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title' , instance.title)
#         instance.description = validated_data.get('description' , instance.description)
#         instance.link = validated_data.get('link' , instance.link)
#         instance.save()
#         return instance

class ServicesSirealizer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    service_icon = serializers.CharField(max_length=50)
    service_title = serializers.CharField(max_length=50)
    service_des=serializers.CharField(max_length=None)

    def create(self, validated_data):
        return Services.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.service_icon = validated_data.get('service_icon' , instance.service_icon)
        instance.service_title = validated_data.get('service_title' , instance.service_title)
        instance.service_des = validated_data.get('service_des' , instance.service_des)
        instance.save()
        return instance
    
    def validate_services_des(self , data):
        if data["services_des"] == "":
            raise serializers.ValidationError({"services_des": "Description field cannot be null"}, data)
        return data