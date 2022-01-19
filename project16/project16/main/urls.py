from django.urls import path
from . import views

urlpatterns = [
    path('', views.show, name="show"),
    path('add_data', views.add_data, name="add_data"),
    path('delete/<str:id>/', views.delete, name="delete"),
    path('update/<str:id>/', views.update, name="update"),


    
]
