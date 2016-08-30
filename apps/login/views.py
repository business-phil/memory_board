from django.shortcuts import render

def index(request):
    return render(request, 'login/index.html')

def register(request):  # POST
    pass

def login(request):  # POST
    pass
