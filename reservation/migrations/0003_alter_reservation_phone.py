# Generated by Django 3.2.9 on 2021-12-07 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_alter_reservation_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='phone',
            field=models.IntegerField(blank=True),
        ),
    ]
