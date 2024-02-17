# Generated by Django 4.2.8 on 2024-02-17 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('date', '0003_alter_dateidea_budget_alter_dateidea_place_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dateidea',
            name='budget',
            field=models.IntegerField(choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')], db_index=True, default=1),
        ),
        migrations.AlterField(
            model_name='dateidea',
            name='description',
            field=models.TextField(db_index=True),
        ),
        migrations.AlterField(
            model_name='dateidea',
            name='name',
            field=models.CharField(db_index=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='dateidea',
            name='place',
            field=models.CharField(choices=[('city', 'City'), ('countryside', 'Countryside'), ('seaside', 'Seaside'), ('park', 'Park'), ('beach', 'Beach')], db_index=True, default='park', max_length=50),
        ),
        migrations.AlterField(
            model_name='dateidea',
            name='time',
            field=models.CharField(choices=[('day', 'Day'), ('night', 'Night')], db_index=True, default='day', max_length=50),
        ),
    ]
