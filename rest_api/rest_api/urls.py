from django.conf.urls import url, include
from rest_framework import routers
from movies import movie_views
from caster import caster_views

router = routers.DefaultRouter()

urlpatterns = [
	url(r'^', include(router.urls)),
	url(r'^movies/', movie_views.MovieList.as_view()),
	url(r'^casters/', caster_views.CasterList.as_view()),
]
