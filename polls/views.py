from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    
    peoples =[
        {'name':"A","age":20},
        {'name':"B","age":30},
        {'name':"C","age":55},
        {'name':"D","age":60},
    ]


    return render(request,"index.html",context={'peoples':peoples})

def success_page(request):
    print("*"*10)
    return HttpResponse("<h1>This is a tutorial</h1>")

def about(request):
    return render(request,'about.html')
