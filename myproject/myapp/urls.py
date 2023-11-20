from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home),
    path('about', views.about),
    path('form', views.form),
    path('edit/<person_id>', views.edit),
    path('delete/<person_id>', views.delete)
]