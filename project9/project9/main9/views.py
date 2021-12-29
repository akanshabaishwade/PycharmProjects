from django.http.request import HttpRequest
from django.shortcuts import render, redirect
from .models import Friends
from django.http import HttpResponse

# Create your views here.

def show_data(request):
    all_data = Friends.objects.all()
    context ={
        'all_data' : all_data
    }

    return render(request, 'show_data.html', context)


def create_data(request):
    if request.method == "POST":
        friend_name = request.POST['name']
        friend_age  = request.POST['age']

        new_data_add = Friends(name=friend_name, age=friend_age)
        new_data_add.save()

        return HttpResponse ("Sucessfully added")

    return render(request, 'create.html')


def delete(request, id):
    if request.method == "POST":
        all_data = Friends.objects.get(pk=id)
        all_data.delete()
        return redirect('/')
