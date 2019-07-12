from django.shortcuts import render,reverse,redirect
from django.template.loader import get_template
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
import datetime
from distutils.command import register
#from django.core.urlresolvers import reverse
# Create your views here.
def index(request):
    return render(request,'index.html')
def usertype(request):
    return render(request,'usertype.html')
def gender(request):
    return render(request,'gender.html')
def frequency(request):
    return render(request,'frequency.html')
def popularity(request):
    return render(request,'popularity.html')
def station(request):
    return render(request,'station.html')
def temperature(request):
    return render(request,'temperature.html')
def weather(request):
    return render(request,'weather.html')
def trip(request):
    return render(request,'trip.html')

def home(request):
    return render(request,'index.html')
def remote(request):
    return render(request,'remote-data.html')
def bikes(request):
    return render(request,'bikes.html')
def lookfoward(request):
    return render(request,'lookforward.html')
def a(request):
    return render(request,'1.html')
def b(request):
    return render(request,'2.html')
def c(request):
    return render(request,'3.html')
def d(request):
    return render(request,'4.html')
def e(request):
    return render(request,'5.html')
def conclude(request):
    return render(request,'conclude.html')