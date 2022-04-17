from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Bb, Rubric

def index(request):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    return render(request, template_name="index.html",
                  context={"bbs": bbs, 'rubrics': rubrics})


def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics,
               'current_rubric': current_rubric}
    return render(request, 'by_rubrics.html', context=context)