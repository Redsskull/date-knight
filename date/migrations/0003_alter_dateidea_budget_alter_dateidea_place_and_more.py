# Generated by Django 4.2.8 on 2024-02-16 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('date', '0002_alter_dateidea_budget_alter_dateidea_place_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dateidea',
            name='budget',
            field=models.IntegerField(choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')], default=1),
        ),
        migrations.AlterField(
            model_name='dateidea',
            name='place',
            field=models.CharField(choices=[('park', 'Park'), ('city', 'City'), ('beach', 'Beach')], default='park', max_length=50),
        ),
        migrations.AlterField(
            model_name='dateidea',
            name='time',
            field=models.CharField(choices=[('day', 'Day'), ('night', 'Night')], default='day', max_length=50),
        ),
    ]
