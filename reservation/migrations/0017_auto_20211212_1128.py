# Generated by Django 3.2.9 on 2021-12-12 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0016_delete_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='email',
            field=models.EmailField(default=False, max_length=254),
        ),
        migrations.AddField(
            model_name='reservation',
            name='phone',
            field=models.IntegerField(default=0),
        ),
    ]
