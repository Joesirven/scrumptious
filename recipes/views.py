from django.shortcuts import render

# Create your views here.

def show_recipe(request):
    return render(request, "recipes/detail.html")
