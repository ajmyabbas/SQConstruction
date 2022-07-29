from django.shortcuts import render

# Create your views here.
def load_home(request):
    return render(request,'home.html')

def internship(request):
    return render(request,'internship.html')   

def learnmore(request):
    return render(request,'learnmore.html')     