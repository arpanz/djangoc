from django.shortcuts import render

def owner(request):
    return render(request, 'polls/owner.html')
