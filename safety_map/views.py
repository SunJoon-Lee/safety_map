from django.shortcuts import render
import folium
import urllib.request
import datetime
import time
import json
import webbrowser
# Create your views here.
def home(request):
    return render(request, 'home.html')

def startpage(request):
    return render(request, 'startpage.html')

def showMaps(request):
    map = folium.Map(location=[37.6511988,127.0161604],zoom_start=12)
    maps=map._repr_html_() 
    return render(request, 'home.html',{'map':maps})

def mypage(request):
    return render(request, 'mypage.html')

def manage_alarm(request):
    return render(request, 'manage_alarm.html')

def manage_danger_map(request):
    return render(request, 'manage_danger_map.html')

def manage_protecter(request):
    return render(request, 'manage_protecter.html')

def danger_map(request):
    return render(request, 'danger_map.html')

def register_danger(request):
    return render(request, 'register_danger.html')