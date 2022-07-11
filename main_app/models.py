from django.db import models
from django.urls import reverse

TESTED = (
  ('?', 'NT'),
  ('P', 'Pos'),
  ('N', 'Neg')
)
# Create your models here.


class Unit(models.Model):
    unit_id = models.CharField(max_length=20)
    ABO = models.CharField(max_length=2)
    D = models.CharField(
        max_length=1,
        choices=TESTED,
        default=TESTED[0][0]
    )
    location = models.CharField(max_length=20)
    shelf = models.IntegerField()

    def __str__(self):
      return self.name

    def get_absolute_url(self):
      return reverse('detail', kwargs={'unit_id': self.id})
