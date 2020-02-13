from django.conf.urls import url, include
from rest_framework import routers
from movies import views

router = routers.DefaultRouter()

urlpatterns = [
	url(r'^', include(router.urls)),
	url(r'^movies/', views.MovieList.as_view()),
]
