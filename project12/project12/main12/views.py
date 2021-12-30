from django.shortcuts import render, redirect
from .models import ColourStore
from django.http import HttpResponse





def show_data(request):
    all_data = ColourStore.objects.all()
    context = {
        'all_data' : all_data
    }
    return render (request, 'show_data.html', context)


def create_data(request):
    if request.method == "POST":
        new_name = request.POST['name']
        new_price = request.POST['price']
        new_type = request.POST['type']

        collect_data = ColourStore(name=new_name, price=new_price,
                                    type=new_type
                                    )
        collect_data.save()

        return HttpResponse("Sucessfully added...!")

    return render (request, 'create_data.html')


def delete_data(request, id):

    ColourStore.objects.get(pk=id).delete()
    return redirect('/')


def update_data(request, id):
    old_data = ColourStore.objects.get(pk=id)

    if request.method == "POST":
        updated_name = request.POST.get('name')
        updated_price = request.POST.get('price')
        updated_type = request.POST.get('type')

        ColourStore.objects.filter(id=id).update(name=updated_name, 
                                                price=updated_price,
                                                type=updated_type
                                                )
        
        return HttpResponse("Sucessfully updated")

    context = {
        'old_data' : old_data
    }

    return render(request, 'update_data.html', context)
