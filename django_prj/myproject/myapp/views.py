from django.shortcuts import render
# from django.http import HttpResponse
from .models import Feature

# Create your views here.
def index(request):
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Feature Name 1'
    feature1.is_true = True
    feature1.details = '1-Ipsum something sommathing...'

    feature2 = Feature()
    feature2.id = 1
    feature2.name = 'Feature Name 2'
    feature2.is_true = False
    feature2.details = '2-Ipsum something sommathing...'

    feature3 = Feature()
    feature3.id = 2
    feature3.name = 'Feature Name 3'
    feature3.is_true = True
    feature3.details = '3-Ipsum something sommathing...'

    features = [feature1, feature2, feature3]

    return render(request, 'index.html', {'features': features})

def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount' : amount_of_words})
