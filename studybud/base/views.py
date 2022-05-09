from django.shortcuts import render
from .models import Room

"""rooms = [
    {'id' : 1, 'name' : 'Lets learn Django!'},
    {'id' : 2, 'name' : 'Lets learn Python!'},
    {'id' : 3, 'name' : 'Lets learn Web Development!'},
]"""

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id = pk)
    context = {'room' : room}
    return render(request, 'base/room.html', context)