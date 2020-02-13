
from rest_framework import viewsets
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MovieSerializer
from .casterSerializers import CasterSerializer
from .models import Movie
from .models import Caster

#class MovieViewSet(viewsets.ModelViewSet):
#	queryset = Movie.objects.all()
#	serializer_class = MovieSerializer

class MovieList(APIView):
	def get(self, request, format=None):
		movies = Movie.objects.all()
		serializer = MovieSerializer(movies, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = MovieSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CasterList(APIView):
	def get(self, request, format=None):
		casters = Caster.objects.all()
		serializer = CasterSerializer(casters, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = CasterSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response("Hello!", status=status.HTTP_201_CREATED)
		return Response("Fail!", status=status.HTTP_400_BAD_REQUEST)
	
