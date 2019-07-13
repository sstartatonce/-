from django.shortcuts import render,reverse,redirect
from django.template.loader import get_template
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
import datetime
from distutils.command import register
import pymysql
from start import models
from django.core import paginator
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

def table(request):
    return render(request,'table.html')
def my_view(request):
    if request.method == 'GET':
        response=HttpResponseRedirect('/table/')
        return response
def my_table(request):
    if request.method=='GET':
        return render(request,'table.html',{{tripduration}})