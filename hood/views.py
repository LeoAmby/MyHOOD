from django.shortcuts import render

# Create your views here.

def index(request):
    news = .objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'index.html', context)
    

def profile(request):
    return render(request, 'profile.html')

