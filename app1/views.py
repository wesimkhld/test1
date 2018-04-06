from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #return HttpResponse ('<em>hellojhh</em>'),
    dict1={'value1':'pass this value from views'}
    return render (request,'app1/i.html',dict1)
# Create your views here.
