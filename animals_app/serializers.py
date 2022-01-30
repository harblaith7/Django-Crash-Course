
# from rest_framework.serializers import Serializer, CharField, IntegerField, FloatField, BooleanField, ValidationError

# from animals_app.models import Animals

# class AnimalSerializer(Serializer):
#     id = IntegerField(read_only=True)
#     name = CharField()
#     type = CharField()
#     weight = FloatField()
#     height = FloatField()
#     gender = BooleanField(default=True)

#     def create(self, data):
#         return Animals.objects.create(**data)

#     def update(self, instance, data):
#         instance.name = data.get('name', instance.name)
#         instance.type = data.get('type', instance.type)
#         instance.weight = data.get('weight', instance.weight)
#         instance.height = data.get('height', instance.height)
#         instance.gender = data.get('gender', instance.gender)

#         instance.save()
#         return instance

#     def validate_name(self, value):
#         if len(value) < 1:
#             raise ValidationError("Name is way too short")
#         return value

#     def validate(self, data):
#         if data['height'] > data['weight']:
#             ValidationError('Height cannot be greater than weight')
#         return data


from django.forms import ValidationError
from rest_framework import serializers
from animals_app.models import Animals, Category


class AnimalSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Animals
        fields = "__all__"

    def validate_name(self, value):
        if len(value) < 1:
            raise ValidationError("Name is way too short")
        return value

    def validate(self, data):
        if data['height'] > data['weight']:
            ValidationError('Height cannot be greater than weight')
        return data
    
    def get_full_name(self, object):
        return object.name + " the " + object.type


class CategorySerializer(serializers.ModelSerializer):
    # animals = AnimalSerializer(many=True, read_only=True)
    animals = serializers.StringRelatedField(many=True)

    class Meta:
        model = Category
        fields = "__all__"
