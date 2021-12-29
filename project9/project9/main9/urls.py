from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_data, name="show_data" ),
    path('create_data', views.create_data, name="create_data" ),
    path('delete/<int:id>/', views.delete, name="delete" ),


]
