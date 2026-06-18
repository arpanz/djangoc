from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    if num_visits > 4:
        del(request.session['num_visits'])

    resp = render(request, 'hello/hello.html', {'num_visits': num_visits})
    resp.set_cookie('dj4e_cookie', '6ae208ea', max_age=1000)
    return resp
