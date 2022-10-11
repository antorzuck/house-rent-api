from rest_framework import serializers
from .models import *


class ImgS(serializers.ModelSerializer):
    class Meta:
        model = Img
        fields = '__all__'


class HouseS(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = '__all__'

