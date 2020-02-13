
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
#from movies.views import MovieViewSet
from movies import views

router = routers.DefaultRouter()
#router.register('movies', MovieViewSet)

urlpatterns = [
	url(r'^', include(router.urls)),
	url(r'^admin/', admin.site.urls),
	url(r'^movie/', views.MovieList.as_view()),
	url(r'^caster/', views.CasterList.as_view()),
]

