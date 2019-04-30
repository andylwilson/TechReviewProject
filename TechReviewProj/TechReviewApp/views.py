from django.shortcuts import render
from .models import TechType, Product, Review

# Create your views here.
def index(request):
    return render(request, 'TechReviewApp/index.html')

def getTypes(request):
    types_list=TechType.objects.all()
    context={'types_list' : types_list}
    return render(request, 'TechReviewApp/types.html', context=context)