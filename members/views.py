from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def sayhello(request):
    return HttpResponse('>>>>>HELLO<<<<<')

def sayhello2(request):
    template = loader.get_template('first.html')
    return HttpResponse(template.render())

def sayfuckyou(request):
    template = loader.get_template('second.html')
    return HttpResponse(template.render())

def mems(request):
    mymember = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers' : mymember,
    }
    return HttpResponse(template.render(context,request))

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
    'mymember' : mymember,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    template = loader.get_template('template.html')
    context = {
        'fruits': ['Apple', 'Banana', 'Cherry'],
    }
    return HttpResponse(template.render(context, request))

def ifa(request):
    template = loader.get_template('indexIFA.html')
    return HttpResponse(template.render())

def testing2(request):
    mydata = Member.objects.values_list('fname')
    #mydata = Member.objects.filter(fname='john').values()
    template = loader.get_template('template2.html')
    context = {
        'mymembers' : mydata
    }
    return HttpResponse(template.render(context, request))