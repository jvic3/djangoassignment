from django.shortcuts import render

# Create your views here.
def animals(request):
    return render(request, 'animals.html')

def porche(request):
    return render(request, 'porche911.html')

def nike(request):
    return render(request, 'nikey.html')