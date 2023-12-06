
from django.urls import path,include
from .views import home, noticias

urlpatterns = [
    path('', home, name='home'),
    path('noticias/<int:id>', noticias, name="noticias")
]