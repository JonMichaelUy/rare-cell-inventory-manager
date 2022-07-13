from django.shortcuts import render, redirect
from .models import Unit
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.db.models import Q



from .forms import UnitSearchForm



def home(request):
  return render(request, 'home.html')


@login_required
def units_index(request):
  units = Unit.objects.all()
  return render(request, 'units/index.html', {'units' : units})

@login_required
def units_detail(request, unit_id):
  unit = Unit.objects.get(id=unit_id)
  return render(request, 'units/detail.html', { 'unit': unit})


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class AddUnit(LoginRequiredMixin, CreateView):
  model = Unit
  fields = '__all__'
  success_url = '/units/'

class  EditUnit(LoginRequiredMixin, UpdateView):
  model = Unit
  fields = '__all__'

class DeleteUnit(LoginRequiredMixin, DeleteView):
  model = Unit
  success_url = '/units/'


class SearchResultsView(LoginRequiredMixin, ListView):
  model = Unit
  template_name = 'search_results.html'

  def get_queryset(self):
    query = self.request.GET.get("q")
    object_list = Unit.objects.filter(
      Q(ABO__icontains=query) | Q(D__icontains=query)
    )
    return object_list