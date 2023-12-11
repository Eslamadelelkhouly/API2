from rest_framework import serializers
from .models import *
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'