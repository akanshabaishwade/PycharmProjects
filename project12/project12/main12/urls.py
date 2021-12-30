from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_data, name="show_data"),
    path('create_data', views.create_data, name="create_data"),
    path('delete_data/<int:id>/', views.delete_data, name="delete_data"),
    path('update_data/<int:id>/', views.update_data, name="update_data"),

]
