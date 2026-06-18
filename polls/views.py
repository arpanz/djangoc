from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. 0147e543 You're at the polls index.")


def owner(request):
    return render(request, 'polls/owner.html')
