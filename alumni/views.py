from django.http import HttpResponse
from django.template import loader
from .models import Alumnus
from django.db.models import Q
from django.shortcuts import render


# Create your views here.
def alumni(request):
    myalumni = Alumnus.objects.all().values()
    template = loader.get_template('all_alumni.html')
    context = {
        'myalumni ': myalumni,
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
    myalumnus = Alumnus.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'myalumnus': myalumnus,
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


def link1(request):
    template = loader.get_template('link1.html')
    return HttpResponse(template.render())


def link2(request):
    template = loader.get_template('link2.html')
    return HttpResponse(template.render())


def link3(request):
    template = loader.get_template('link3.html')
    return HttpResponse(template.render())


def index(request):
    if request.method == "GET":
        if 'q' in request.GET:
            q = request.GET['q']
            # data = Data.objects.filter(first_name__icontains=q)
            multiple_q = Q(Q(firstname__icontains=q) | Q(lastname__icontains=q))
            alumnus = Alumnus.objects.filter(multiple_q)
        else:
            alumnus = Alumnus.objects.all()
        context = {
            'alumnus': alumnus,
            'q': q
        }
    # template = loader.get_template('index.html')
    # return HttpResponse(request, template.render(), context)
    return render(request, 'index.html', context)
