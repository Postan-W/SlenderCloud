from django.shortcuts import render
from django.http import HttpResponse
def index(request):
     return HttpResponse('<h1>author: Wang Mingzhu 2019.4.19</h1>')