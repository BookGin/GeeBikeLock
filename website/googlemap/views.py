from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Bike, User2bike
import math
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
    bike.is_stolen = False
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

def check_moving(x1, y1, z1, x2, y2, z2):
    thr = 0
    if math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2) > thr:
        return True
    else:
        return False

def update_uid(uid,  recv_uid):
    if uid == 0:
        return recv_uid
    else:
        return uid

def update(request, bike_id):
    recv_data = json.loads(request.body.decode())
    bike, created = Bike.objects.get_or_create(name = bike_id)
    bike.lat, bike.lng = recv_data['gps'][0], recv_data['gps'][1]
    if check_moving(bike.x, bike.y, bike.z, recv_data['axis'][0], recv_data['axis'][1], recv_data['axis'][2]):
        bike.moving_count += 1
    else:
        bike.moving_count = 0
    bike.x,  bike.y,  bike.z = recv_data['axis'][0],  recv_data['axis'][1],  recv_data['axis'][2]
    bike.uid = update_uid(bike.uid, recv_data['uid'])
    if bike.uid != 0 and bike.uid == recv_data['uid']:
        bike.available = False if bike.available else True
    print(bike.moving_count)
    if bike.moving_count > 0 and bike.available == False:
        bike.is_stolen = True
    if bike.available == True:
        bike.is_stolen = False
    bike.save()

    return JsonResponse({'available': bike.available, 'is_stolen': bike.is_stolen})

def list(request):
    bikes = request.user.own_bike.all()
    return render(request, 'list.html', {'bikes': bikes})

def register_bike(request):
    if request.method == 'POST':
        user, bike_id = request.user, request.POST.get("bike_id", "")
        newbike, created = Bike.objects.get_or_create(user = user, name = bike_id)
        #newbike = Bike.objects.create(user=user, name=bike_id)
        newbike.save()

        return redirect(reverse('index'))
    else:
        return render(request, 'register_bike.html')
