# Generated by Django 4.0.6 on 2022-07-13 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_unit_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='date',
            field=models.DateField(null=True, verbose_name='Expires'),
        ),
    ]