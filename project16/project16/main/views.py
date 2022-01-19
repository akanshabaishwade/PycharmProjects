
import re
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import PersonDetails
# Create your views here.
def show(request):
    all_data = PersonDetails.objects.all()
    context = {
        'all_data': all_data
    }
    return render(request, 'show.html', context)

def add_data(request):
    if request.method == "POST":
        new_name = request.POST['name']
        new_age = request.POST['age']

        new_all_data = PersonDetails(name=new_name, age=new_age)
        new_all_data.save()

        return HttpResponse("Done")


        
    return render(request, 'create.html')


def delete(request, id):
    PersonDetails.objects.get(id=id).delete()
    return redirect('/')

def update(request, id):
    form = PersonDetails.objects.get(id=id)

    if request.method == "POST":
        update_name = request.POST.get('name')
        update_age = request.POST.get('age')

        PersonDetails.objects.filter(id=id).update(name=update_name, age=update_age)
        return redirect('/')

    context = {
        'form': form
    }

    return render(request, 'update.html', context)