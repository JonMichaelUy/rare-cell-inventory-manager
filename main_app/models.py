from django.db import models

TESTED = (
    ('P', 'Pos'),
    ('N', 'Neg'),
    ('?', 'NT'),
)
# Create your models here.


class Unit(models.Model):
    unit_id = models.CharField(max_length=20)
    ABO = models.CharField(max_length=2)
    D = models.CharField(
        max_length=1,
        choices=TESTED,
        default=TESTED[1][1]
    )
    location = models.CharField(max_length=20)
    shelf = models.IntegerField()

    def __str__(self):
      return self.name
