from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Pet
from .forms import PetForm
def pet_list(request):
    list = Pet.objects.all()
    list = [x for x in list if x.available]
    paginator = Paginator(list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'list.html', {'pets': page_obj})

def pet_detail(request, pet_id):
    pet =Pet.objects.get(id=pet_id)
    context = {
                "pet": pet
    }
    return render(request, 'detail.html', context)

def pet_create(request):
    form = PetForm()
    if request.method == "POST":
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pet-list')
    context = {
        "form":form,
    }
    return render(request, 'create.html', context)
def pet_update(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    form = PetForm(instance=pet)
    if request.method == "POST":
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet-list')
    context = {
        "pet":pet,
        "form":form,
    }
    return render(request, 'update.html', context)
def pet_delete(request, pet_id):
    Pet.objects.get(id=pet_id).delete()
    return redirect("pet-list")
