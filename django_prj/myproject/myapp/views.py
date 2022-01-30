from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def index(request): # assigned to homepage
    name = 'Tester'
    context = {
        'name': 'Tester',
        'age': 42,
        'occupation': 'Human'
    }
    return render(request, 'index.html', context)
