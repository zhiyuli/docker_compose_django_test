from django.conf.urls import url
from my_first_app import views

urlpatterns = [
    url(r'^$', views.home),
    ]