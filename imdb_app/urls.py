from django.contrib import admin
from django.urls import path, include

from imdb_app import views

# http://127.0.0.1:8000/api/imdb/movies
# movies

# http://127.0.0.1:8000/api/imdb/movies/3
# http://127.0.0.1:8000/api/imdb/movies/327

urlpatterns = [
    path('movies', views.get_movies),
    path('movies/<int:movie_id>', views.get_movie),
    path('movies/<int:movie_id>/actors', views.get_movie_actors),

    path('actors', views.get_actors),

    path('ratings', views.get_ratings),
    path('movies/<int:movie_id>/ratings', views.get_movie_ratings),
    path('movies/<int:movie_id>/ratings/avg', views.get_avg_movie_rating),
]
