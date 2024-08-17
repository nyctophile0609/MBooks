from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

class BooksModelSerializer(ModelSerializer):
    class Meta:
        model=BooksModel
        fields="__all__"
        