from django.shortcuts import render


def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')


def contact(request):
    return render(request, 'pages/contact.html')


def portfolio(request):
    return render(request, 'pages/portfolio.html')


def resume(request):
    return render(request, 'pages/resume.html')


def services(request):
    return render(request, 'pages/services.html')


