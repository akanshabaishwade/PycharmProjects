from django.urls import path
from . import views

urlpatterns = [
    path('', views.show, name="show"),
    path('create', views.create, name="create"),
    path('detele/<int:id>/', views.detele, name="detele"),
    path('update/<int:id>/', views.update, name="update"),


]
