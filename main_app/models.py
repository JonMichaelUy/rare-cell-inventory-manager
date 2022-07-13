from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

TESTED = (
  ('NT', 'Not Tested'),
  ('+', 'Positive'),
  ('-', 'Negative')
)
# Create your models here.


class Unit(models.Model):
    unit_id = models.CharField(max_length=20)
    ABO = models.CharField(max_length=2)
    D = models.CharField(
        max_length=5,
        choices=TESTED,
        default=TESTED[0][0]
    )
    C = models.CharField(
        max_length=5,
        choices=TESTED,
        default=TESTED[0][0]
    )
    Cw = models.CharField(
        max_length=5,
        choices=TESTED,
        default=TESTED[0][0]
    )
    E = models.CharField(
        max_length=5,
        choices=TESTED,
        default=TESTED[0][0]
    )
    c = models.CharField(
        max_length=5,
        choices=TESTED,
        default=TESTED[0][0]
    )
    e = models.CharField(
        max_length=5,
        choices=TESTED,
        default=TESTED[0][0]
    )
    K = models.CharField(
        max_length=5,
        choices=TESTED,
        default=TESTED[0][0]
    )
    k = models.CharField(
        max_length=5,
        choices=TESTED,
        default=TESTED[0][0]
    )
    Kpa = models.CharField(
        max_length=5,
        choices=TESTED,
        default=TESTED[0][0]
    )
    Kpb = models.CharField(
        max_length=5,
        choices=TESTED,
        default=TESTED[0][0]
    )
    Jsa = models.CharField(
        max_length=5,
        choices=TESTED,
        default=TESTED[0][0]
    )
    Jsb = models.CharField(
        max_length=5,
        choices=TESTED,
        default=TESTED[0][0]
    )
    Fya = models.CharField(
        max_length=5,
        choices=TESTED,
        default=TESTED[0][0]
    )
    Fyb = models.CharField(
        max_length=5,
        choices=TESTED,
        default=TESTED[0][0]
    )
    Fy3 = models.CharField(
        max_length=5,
        choices=TESTED,
        default=TESTED[0][0]
    )
    Jka = models.CharField(
        max_length=5,
        choices=TESTED,
        default=TESTED[0][0]
    )
    Jkb = models.CharField(
        max_length=5,
        choices=TESTED,
        default=TESTED[0][0]
    )
    Jk3 = models.CharField(
        max_length=5,
        choices=TESTED,
        default=TESTED[0][0]
    )
    Dia = models.CharField(
        max_length=5,
        choices=TESTED,
        default=TESTED[0][0]
    )
    Dib = models.CharField(
        max_length=5,
        choices=TESTED,
        default=TESTED[0][0]
    )
    Wra = models.CharField(
        max_length=5,
        choices=TESTED,
        default=TESTED[0][0]
    )
    Wrb = models.CharField(
        max_length=5,
        choices=TESTED,
        default=TESTED[0][0]
    )
    Lea = models.CharField(
        max_length=5,
        choices=TESTED,
        default=TESTED[0][0]
    )
    Leb = models.CharField(
        max_length=5,
        choices=TESTED,
        default=TESTED[0][0]
    )
    M = models.CharField(
        max_length=5,
        choices=TESTED,
        default=TESTED[0][0]
    )
    N = models.CharField(
        max_length=5,
        choices=TESTED,
        default=TESTED[0][0]
    )
    S = models.CharField(
        max_length=5,
        choices=TESTED,
        default=TESTED[0][0]
    )
    s = models.CharField(
        max_length=5,
        choices=TESTED,
        default=TESTED[0][0]
    )
    U = models.CharField(
        max_length=5,
        choices=TESTED,
        default=TESTED[0][0]
    )
    location = models.CharField(max_length=20)
    shelf = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
      return self.name

    def get_absolute_url(self):
      return reverse('detail', kwargs={'unit_id': self.id})
