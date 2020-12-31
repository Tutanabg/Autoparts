import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.http import JsonResponse
from django.core import serializers
from django.core.serializers import serialize
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


B = Body.objects.all();
	
D = Doors.objects.all();
	
AV = AVDevices.objects.all();
	
C = Cameras.objects.all();
	
W = Windows.objects.all();

def index(request):
	return render(request, 'autoparts/index.html',{'B': B, 'D': D, 'AV': AV, 'C': C, 'W': W})
	

def newparts(request):
	return render(request, 'autoparts/newparts.html',{'B': B, 'D': D, 'AV': AV, 'C': C, 'W': W})
	
	
		
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["Username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "autoparts/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "autoparts/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["Username"]
        

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "autoparts/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, password)
            user.save()
        except IntegrityError:
            return render(request, "autoparts/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "autoparts/register.html")

def pay(request):
	return render(request, 'autoparts/pay.html')
	
def parts(request, item):
	b = Body.objects.get(body_name=item)
	return render(request, 'autoparts/parts.html',{'item':b})
	
	
def bodyapi(request):
	B = Body.objects.all();
	return JsonResponse([Body.serialize() for Body in B], safe=False)
	
	
def body(request, item):
	B = Body.objects.filter(body_name=item).last();
	return render(request, 'autoparts/pay.html', {'d':B})
	
	
def doorsapi(request):
	D= Doors.objects.all();
	return JsonResponse([Doors.serialize() for Doors in D], safe=False)
	
	
def doors(request, item):
	D= Doors.objects.filter(doors_name=item).last();
	return render(request, 'autoparts/pay.html', {'d':D})
	
	
def avdevicesapi(request):
	AV= AVDevices.objects.all();
	return JsonResponse([AVDevices.serialize() for AVDevices in AV], safe=False)
	
	
def avdevices(request, item):
	AV= AVDevices.objects.filter(av_name=item).last();
	return render(request, 'autoparts/pay.html', {'d':AV})
	
	
def camerasapi(request):
	C= Cameras.objects.all();
	return JsonResponse([Cameras.serialize() for Cameras in C], safe=False)
	
	
def cameras(request, item):
	C= Cameras.objects.filter(cameras_name=item).last();
	return render(request, 'autoparts/pay.html', {'d':C})
	
	
def windowsapi(request):
	W= Windows.objects.all();
	return JsonResponse([Windows.serialize() for Windows in W], safe=False)
	
	
def windows(request, item):
	W= Windows.objects.filter(windows_name=item).last();
	return render(request, 'autoparts/pay.html', {'d':W})
	
	
	
@csrf_exempt
def payment(request): 
	data = json.loads(request.body)
	a = data.get("name")     
	b = data.get("price")
	c = data.get("card_number")
	pay = Payment(
	name = a,   
	price = b,
	card_number = c,
	)
	pay.save()
	return JsonResponse(pay.serialize(), safe=False)
	

@csrf_exempt
def newbody(request):
	data = json.loads(request.body)
	a = data.get("body_name")     
	b = data.get("body_price")
	body = Body(
	body_name = a,   
	body_price = b,
	)
	body.save()
	return JsonResponse(body.serialize(), safe=False)

		
@csrf_exempt
def newdoor(request):
	data = json.loads(request.body)
	a = data.get("doors_name")     
	b = data.get("doors_price")
	door = Doors(
	doors_name = a,   
	doors_price = b,
	)
	door.save()
	return JsonResponse(door.serialize(), safe=False)
	
	
	
@csrf_exempt
def newav(request):
	data = json.loads(request.body)
	a = data.get("av_name")     
	b = data.get("av_price")
	av = AVDevices(
	av_name = a,   
	av_price = b,
	)
	av.save()
	return JsonResponse(av.serialize(), safe=False)
	
	
	
@csrf_exempt
def newcamera(request):
	data = json.loads(request.body)
	a = data.get("cameras_name")     
	b = data.get("cameras_device")
	camera = Cameras(
	cameras_name = a,   
	cameras_price = b,
	)
	camera.save()
	return JsonResponse(camera.serialize(), safe=False)
	
	
	
@csrf_exempt
def newwindow(request):
	data = json.loads(request.body)
	a = data.get("windows_name")     
	b = data.get("windows_price")
	window = Windows(
	windows_name = a,   
	windows_price = b,
	)
	window.save()
	return JsonResponse(window.serialize(), safe=False)
	
