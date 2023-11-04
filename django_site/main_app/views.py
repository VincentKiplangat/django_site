from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"index.html")


def shop(request):
    return render(request,"shop.html")


def about(request):
    return render(request,"about.html")


def contact(request):
    return render(request, "contact.html")


def faq(request):
    return render(request,"faq.html")