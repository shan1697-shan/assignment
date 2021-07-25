from django.db.models import query
from django.shortcuts import render
from .models import Devicedata

def index(request):
    query = Devicedata.objects.all()
    query=query[::-1]
    l = []
    data = []
    for i in query:
        if i.imei not in l:
            l.append(i.imei)
            if i.soc<20:
                colour = 'red'
            else:
                colour = 'white'
            if i.packv>100:
                pcolour = 'red'
            else:
                pcolour = 'white'
            data.append([i.imei,i.soc,i.packv,i.created_on,colour,pcolour])
    return render(request, 'app/index.html', {"devices":data})

def room(request, room_name):
    return render(request, 'app/room.html', {
        'room_name': room_name
    })