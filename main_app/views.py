
from ast import And
from django.shortcuts import render, redirect
from .models import Unit
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import UnitSearchForm
from django.http import HttpResponse
from django.db.models import Q


from django.views.generic import TemplateView, ListView

# Create your views here.
def home(request):
  return render(request, 'home.html')



def units_index(request):
  units = Unit.objects.all()
  return render(request, 'units/index.html', {'units' : units})

def units_detail(request, unit_id):
  unit = Unit.objects.get(id=unit_id)
  return render(request, 'units/detail.html', { 'unit': unit})


class AddUnit(CreateView):
  model = Unit
  fields = '__all__'
  success_url = '/units/'

class  EditUnit(UpdateView):
  model = Unit
  fields = '__all__'

class DeleteUnit(DeleteView):
  model = Unit
  success_url = '/units/'


class SearchResultsView(ListView):
  model = Unit
  template_name = 'search_results.html'

  def get_queryset(self):
    query = self.request.GET.get("q")
    object_list = Unit.objects.filter(
      Q(ABO__icontains=query) | Q(D__icontains=query)
    )
    return object_list