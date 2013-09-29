from django.shortcuts import render
from jsonview.decorators import json_view

def home(request):
    return render(request, 'room_list.html', {})

def room_list(request):
    return render(request, '', {'list': None})