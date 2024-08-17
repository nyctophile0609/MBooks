from rest_framework.response import Response
from rest_framework import status, permissions, authentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import *
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .serializers import *
from .models import *
from django.http import JsonResponse

class BooksModelViewSet(ModelViewSet):
    queryset=BooksModel.objects.all()
    serializer_class=BooksModelSerializer
    