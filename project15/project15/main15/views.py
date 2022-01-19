from typing import AsyncGenerator, overload
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import StudentData
from django.http import HttpResponse


def show(request):
    all_data = StudentData.objects.all()
    context = {
        'all_data': all_data
    }
    return render(request, 'show.html', context)

def create(request):
    if request.method == "POST":
        new_name = request.POST['name']
        new_class = request.POST['class']
        new_age = request.POST['age']

        all_new_data = StudentData(name=new_name, Class=new_class, age=new_age)
        all_new_data.save()

        return HttpResponse("Sucessfully created...!")

    return render(request, 'create.html')

def detele(request, id):
    StudentData.objects.get(id=id).delete()
    return redirect ('/')


def update(request, id):

    old_data = StudentData.objects.filter(pk=id)

    if request.method == "POST":
        update_name = request.POST.get('name')
        update_class = request.POST.get('class')
        update_age = request.POST.get('age')

        StudentData.objects.filter(pk=id).update(name=update_name, Class=update_class, age=update_age)
        return redirect ('/')
    
    context = {
        'old_data': old_data
    }
    return render(request, 'update.html', context)
