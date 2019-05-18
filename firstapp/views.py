from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from .models import Wardrobe
from weather.app import get_clothes
import requests
import json


# Wardrobe dictionary
WARDROBE = {'1': 'T-shirt', '2': 'Sweater', '3': 'Jacket',
            '4': 'Warm pants', '5': 'Jeans', '6': 'Shorts',
            '7': 'Slippers', '8': 'Shoes', '9': 'Sneakers'
            }


# Create your views here.
def GetWeather(request, from_point, to_point):
    from_point = from_point[1:len(from_point) - 1]
    to_point = to_point[1:len(to_point) - 1]
    r = requests.get('https://maps.googleapis.com/maps/api/directions/json?'
                        'origin={}&destination={}&'
                        'key=AIzaSyCVfcHKE8xYy98PU-wvAI43z6wzejf9K5I'.format(from_point, to_point))

    f = open('index.txt', 'w')
    f.write(str(r.content))
    from_coor = tuple([float(el) for el in from_point.split(', ')])
    to_coor = tuple([float(el) for el in to_point.split(', ')])
    data = {'clothes': get_clothes([from_coor, to_coor])}
    return render(request, 'clothes.html', context=data)


def profile(request):
    user_email = request.user.email
    try:
        print('User has wardrobe')
        user_wardrobe = Wardrobe.objects.get(email=user_email).clothes
    except Wardrobe.DoesNotExist:
        print('User has not wardrobe')
        user_wardrobe = []

    data = {'clothes': []}
    for ch in user_wardrobe:
        if ch.isdigit():
            data['clothes'].append(WARDROBE[ch])

    return render(request, 'profile.html', context=data)


def main_page(request):
    return render(request, 'main.html')


@csrf_protect
def change_wardrobe(request):
    if request.method == "POST":
        clothes = ','.join(json.loads(request.POST['checkboxes']))
        email = request.user.email
        print(clothes, request.user.email)

        try:
            user = Wardrobe.objects.get(email=email)
            user.clothes = clothes
            user.save()
            print('Edit wardrobe..')
        except Wardrobe.DoesNotExist:
            user = Wardrobe.objects.create(email=request.user.email, clothes=clothes)
            user.save()
            print('Create wardrobe..')

        return HttpResponse('')


