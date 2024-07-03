from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.



def logout_page(request):
    logout(request)
    return redirect('/login_page/')

def login_page(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not User.objects.filter(username=username).exists():
            messages.error(request,'invalid username')
            return redirect('/login_page/')
        user = authenticate(username=username,password=password)
        if user is None:
            messages.error(request,"invalid password")
            return redirect('/login_page/')
        else:
            messages.info(request,'login successful')
            login(request,user)
            return redirect('/receipes/')

        



    return render(request,'login_page.html')


def registration_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user=User.objects.filter(username=username)
        if user.exists():
            messages.info(request,"User already exists")

            return redirect('/registration_page/')

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        user.set_password(password)
        user.save()
        messages.info(request,"Account created successfully")
        return redirect('/registration_page/')

    return render(request,'registration_page.html')

@login_required(login_url='/login_page/')
def receipes(request):
    

    if request.method == 'POST':
        data=request.POST
        receipe_name=data.get('receipe_name')
        receipe_description=data.get('receipe_description')
        receipe_image=request.FILES.get('receipe_image')
        print(data)


        print('receipe_name: ',receipe_name)
        print('receipe_description: ',receipe_description)
        print('receipe_image: ',receipe_image)

        Receipe.objects.create(
            receipe_name=receipe_name,
            receipe_description=receipe_description,
            receipe_image=receipe_image

        )
        return redirect('/receipes')
    
    queryset=Receipe.objects.all()

    if request.GET.get('search_food'):
        print('search food name: ',request.GET.get('search_food'))
        queryset=queryset.filter(receipe_name__icontains = request.GET.get('search_food'))



    context={'receipes':queryset}

    return render(request,"receipes.html",context=context)


def update_receipes(request,id):
    queryset=Receipe.objects.get(id=id)
    print("queryset:",queryset)
    

    if request.method == 'POST':
        data=request.POST
        receipe_name=data.get('receipe_name')
        receipe_description=data.get('receipe_description')
        receipe_image=request.FILES.get('receipe_image')
        print(data)

        queryset.receipe_name=receipe_name
        queryset.receipe_description=receipe_description
        if receipe_image:
            queryset.receipe_image=receipe_image
        queryset.save()
        return redirect('/receipes/')


    
    context={'receipes':queryset}
    print("context: ",context)


    return render(request,"update_receipes.html",context=context)

def delete_receipe(request,id):
    print(id)
    queryset=Receipe.objects.get(id=id)
    queryset.delete()
    # return HttpResponse('a')
    return redirect('/receipes/')
