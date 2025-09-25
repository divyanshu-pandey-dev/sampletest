from django.shortcuts import get_object_or_404, render, redirect
from .models import mark1, mark2, poster
# Create your views here.
def index(request):
    data = mark1.objects.all()
    return render(request,'index.html',{'data':data})
def shop(request):
    data = mark2.objects.all()
    return render(request,'shop.html',{'data':data})
def blog(request):
    data = poster.objects.all()
    return render(request,'blog.html',{'data':data})

def checkout(request,id):
    product = get_object_or_404(mark2,id=id)
    return render(request, 'checkout.html',{'product':product})

def cart(request,id):
    product1 = get_object_or_404(mark2,id=id)
    return render(request, 'cart.html',{'product1':product1})