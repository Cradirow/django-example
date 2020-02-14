from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CasterSerializer
from .models import Caster

class CasterList(APIView):
	def get(self, request, format=None):
		casters = Caster.objects.all()
		serializer = CasterSerializer(casters, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = CasterSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
