from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Bike, User2bike

import json
def index(request):
    gpss = []
    for bike in Bike.objects.all():
        gpss.append({'lat': bike.lat, 'lng': bike.lng})
    if len(request.user.own_bike.all()) > 0:
        user_bike = request.user.own_bike.all()[0]
        gps_center = {'lat': user_bike.lat, 'lng': user_bike.lng}
    else:
        gps_center = {'lat': 25.074132, 'lng': 121.522084}
    return render(request, 'index.html', {'gpss': gpss, 'gps_center': gps_center})

def unlock(request, bike_id):
    bike = Bike.objects.get(name = bike_id)
    bike.available = True
    bike.save()
    return redirect(reverse('index'))

def lock(request,  bike_id):
    bike = Bike.objects.get(name = bike_id)
    bike.available = False
    bike.save()
    return redirect(reverse('index'))

def remove(request,  bike_id):
    bike = Bike.objects.get(name = bike_id).delete()
    return redirect(reverse('index'))

def update(request, bike_id):
    recv_data = json.loads(request.body.decode())
    bike, created = Bike.objects.get_or_create(name = bike_id)
    bike.lat, bike.lng = recv_data['gps'][0], recv_data['gps'][1]
    bike.save()

    return JsonResponse({'available': bike.available})

def list(request):
    bikes = request.user.own_bike.all()
    bikes = [ {'name': bike.name, 'available': bike.available} for bike in bikes]
    return render(request, 'list.html', {'bikes': bikes})

def register_bike(request):
    if request.method == 'POST':
        user, bike_id = request.user, request.POST.get("bike_id", "")
        newbike = Bike.objects.create(user=user, name=bike_id)
        newbike.save()

        return redirect(reverse('index'))
    else:
        return render(request, 'register_bike.html')
