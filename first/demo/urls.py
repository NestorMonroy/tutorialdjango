from django.conf.urls import include, url
from django.urls import path
from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register('books', views.BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
