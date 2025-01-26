from django.urls import path 
from .views import home, python, test, name, temp1, portfolio, login, test1


urlpatterns = [
    path("world/", home),
    path("python/", python),
    path("test/", name),
    path("test1/", test1),
    path("temp/", temp1),
    path("portfolio/", portfolio),
    path("login/", login),
    path("", home)
]