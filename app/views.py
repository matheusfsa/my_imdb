from rest_framework import generics
from .models import Movie
from .serializers import MovieSerializer
from django.shortcuts import render


def home(request):
    return render(request, 'app/home.html')


class MovieList(generics.ListCreateAPIView):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

