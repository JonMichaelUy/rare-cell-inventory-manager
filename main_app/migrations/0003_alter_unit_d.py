# Generated by Django 4.0.6 on 2022-07-11 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_unit_d'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='D',
            field=models.CharField(choices=[('NT', 'Not Tested'), ('+', 'Positive'), ('-', 'Negative')], default='NT', max_length=5),
        ),
    ]