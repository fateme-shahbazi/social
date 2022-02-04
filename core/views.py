from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from . import serializers
from core.models import Profile, Post, Comment, Like, Relation


