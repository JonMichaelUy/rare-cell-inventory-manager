
from django.shortcuts import render
from .models import Unit



# Create your views here.
def home(request):
  return render(request, 'home.html')

# class Unit:
#   def __init__ (self, unit_id, ABO, D, location, shelf):
#     self.unit_id = unit_id
#     self.ABO = ABO
#     self.D = D
#     self.location = location
#     self.shelf = shelf

# units = [
#   Unit('W1202ABC123', 'A', 'Pos', 'Harris Freezer', 9),
#   Unit('W1204RBC324', 'O', 'Pos', 'Harris Freezer', 4),
#   Unit('W1203ERD123', 'B', 'Pos', 'Harris Fridge', 2),
#   ]
  

def units_index(request):
  units = Unit.objects.all()
  return render(request, 'units/index.html', {'units' : units})

def units_detail(request, unit_id):
  unit = Unit.objects.get(id=unit_id)
  return render(request, 'units/detail.html', { 'unit': unit})