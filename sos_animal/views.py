from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Pet
from django.contrib.auth import logout


@login_required(login_url='/login/')
def logout_user(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/login/')
def register_submit(request):
    city = request.POST.get('city')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    description = request.POST.get('description')
    file = request.FILES.get('file')
    user = request.user
    pet_id = request.POST.get('pet_id')
    if pet_id:
        pet = Pet.objects.get(id=pet_id)
        if user == pet.user:
            pet.email = email
            pet.phone = file
            pet.city = city
            pet.description = description
            if file:
                pet.photo = file
            pet.save()
    else:
        pet = Pet.objects.create(email=email, phone=phone, city=city, description=description,
                                user=user, file=file)
    url = '/pet/detail/{}/'.format(pet.id)
    return redirect(url)


@login_required(login_url='/login/')
def register_pet(request):
    pet_id = request.GET.get('id')
    if pet_id:
        pet = Pet.objects.get(id=pet_id)
        if pet.user == request.user:
            return render(request, 'register.html', {'pet':pet})
    return render(request, 'register.html')


@login_required(login_url='/login/')
def pet_detail(request, id):
    pet = Pet.objects.get(active=True, id=id)
    return render(request, 'pet.html', {'pet':pet})


@login_required(login_url='/login/')
def list_all_pet(request):
    pet = Pet.objects.filter(active=True)
    return render(request, 'list.html', {'pet':pet})


@login_required(login_url='/login/')
def list_user_pet(request):
    pet = Pet.objects.filter(active=True, user=request.user)
    return render(request, 'list.html', {'pet':pet})


@login_required(login_url='/login/')
def delete_pet(request, id):
    pet = Pet.objects.get(id=id)
    if pet.user == request.user:
        pet.delete()
    return redirect('/')


def login_user(request):
    return render(request, 'login.html')


@csrf_protect
def submit_login(request):
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/pet/all/')
        else:
            messages.error(request, 'Usuário/Senha inválidos. Favor tentar novamente.')
    return redirect('/login/')
