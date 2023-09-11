from django.shortcuts import render, HttpResponse


def home(request):
    return render(request, 'index.html')


def test(request):
    print(request)
    return HttpResponse("<script>alert('Working Fine')</script>")


def not_found(request, exception):
    return render(request, '404.html')
