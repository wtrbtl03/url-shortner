from django.shortcuts import render, redirect, HttpResponse
from maps.input_field_form import InputField

def home(request):
    form = InputField()
    return render(request, 'index.html', context={'form' : form})

def test(request):
    print(request)
    return HttpResponse("<script>alert('gand marao')</script>")

def not_found(request, exception):
    return render(request, '404.html')


