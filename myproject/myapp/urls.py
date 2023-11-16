from django.urls import path
from .views import home,about,form

urlpatterns = [
    path('', home),
    path('about', about),
    path('form', form)
]