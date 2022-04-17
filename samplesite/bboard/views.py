from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
# Create your views here.
from .models import Bb, Rubric
from bboard.forms.form import BbForm

def index(request):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    return render(request, template_name="bboard/index.html",
                  context={"bbs": bbs, 'rubrics': rubrics})


def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics,
               'current_rubric': current_rubric}
    return render(request, 'bboard/by_rubrics.html', context=context)


class BbCreateView(CreateView):
    template_name = "bboard/create.html"
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context
