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
  fields = ['unit_id', 'date', 'ABO', 'D', 'C', 'Cw', 'E', 'c', 'e', 'K', 'k', 'Kpa', 'Kpb', 'Jsa', 'Jsb', 'Fya', 'Fyb', 'Fy3', 'Jka', 'Jkb', 'Jk3', 'Dia', 'Dib', 'Wra', 'Wrb', 'Lea', 'Leb', 'M', 'N', 'S', 's', 'U', 'location', 'shelf', 'notes', 'user']
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
    ABO = self.request.GET.get("ABO")
    D = self.request.GET.get("D")
    C = self.request.GET.get("C")
    Cw = self.request.GET.get("Cw")
    E = self.request.GET.get("E")
    c = self.request.GET.get("c")
    e = self.request.GET.get("e")
    K = self.request.GET.get("K")
    k = self.request.GET.get("k")
    Kpa = self.request.GET.get("Kpa")
    Kpb = self.request.GET.get("Kpb")
    Jsa = self.request.GET.get("Jsa")
    Jsb = self.request.GET.get("Jsb")
    Fya = self.request.GET.get("Fya")
    Fyb = self.request.GET.get("Fyb")
    Fy3 = self.request.GET.get("Fy3")
    Jka = self.request.GET.get("Jka")
    Jkb = self.request.GET.get("Jkb")
    Jk3 = self.request.GET.get("Jk3")
    Dia = self.request.GET.get("Dia")
    Dib = self.request.GET.get("Dib")
    Wra = self.request.GET.get("Wra")
    Wrb = self.request.GET.get("Wrb")
    Lea = self.request.GET.get("Lea")
    Leb = self.request.GET.get("Leb")
    M = self.request.GET.get("M")
    N = self.request.GET.get("N")
    S = self.request.GET.get("S")
    s = self.request.GET.get("s")
    U = self.request.GET.get("U")
    object_list = Unit.objects.filter(
      Q(ABO__icontains=ABO) & Q(D__icontains=D) & Q(C__icontains=C) & Q(Cw__icontains=Cw) & Q(E__icontains=E) & Q(c__icontains=c) & Q(e__icontains=e) & Q(K__icontains=K) & Q(k__icontains=k) & Q(Kpa__icontains=Kpa) & Q(Kpb__icontains=Kpb) & Q(Jsa__icontains=Jsa) & Q(Jsb__icontains=Jsb) & Q(Fya__icontains=Fya) & Q(Fyb__icontains=Fyb) & Q(Fy3__icontains=Fy3) & Q(Jka__icontains=Jka) & Q(Jkb__icontains=Jkb) & Q(Jk3__icontains=Jk3) & Q(Dia__icontains=Dia) & Q(Dib__icontains=Dib) & Q(Wra__icontains=Wra) & Q(Wrb__icontains=Wrb) & Q(Lea__icontains=Lea) & Q(Leb__icontains=Leb) & Q(M__icontains=M) & Q(N__icontains=N) & Q(S__icontains=S) & Q(s__icontains=s) & Q(U__icontains=U)
    )
    return object_list