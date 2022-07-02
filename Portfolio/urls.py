from django.urls import path
from . import views

app_name = "Portfolio"
urlpatterns = [
    path('', views.home, name='home'),
    path('portfolio/<int:id>/', views.detail, name='detail'),
]