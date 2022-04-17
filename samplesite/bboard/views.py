from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Bb

def index(request):
    bb = Bb.objects.order_by('-published')
    return render(request, template_name="index.html", context={"bbs": bb})

