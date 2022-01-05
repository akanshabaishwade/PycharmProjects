from django.shortcuts import redirect, render
from .models import WeddingInvitation
from django.http import HttpResponse



# Create your views here.

def show(request):
    data_show = WeddingInvitation.objects.all()
    context = {
        'data_show': data_show
    }
    return render (request, 'show.html', context)

def create(request):
    if request.method == "POST":
        new_name = request.POST['name']
        new_relation = request.POST['relation']
        new_rating = request.POST['rating']

        create_data = WeddingInvitation(name=new_name, relation=new_relation,
                                        gift_rating=new_rating,
                                        )
        create_data.save()
        
        return HttpResponse("Sucessfully created..!")

    return render (request, 'create.html')



def update(request, id):

    old_data = WeddingInvitation.objects.get(pk=id)

    if request.method == "POST":
        updated_name = request.POST.get('name')
        updated_relation = request.POST.get('relation')
        updated_rating = request.POST.get('rating')

        WeddingInvitation.objects.filter(id=id).update(name=updated_name,
                                                        relation=updated_relation,
                                                        gift_rating=updated_rating
                                                        )
        return HttpResponse("Sucessfully ..!")


    context = {
        'old_data': old_data,
    }
    return render (request, 'update.html', context)


def delete(request, id):

    WeddingInvitation.objects.filter(id=id).delete()
    # return redirect('/create')
    return HttpResponse("Sucessfully ..!")





    

