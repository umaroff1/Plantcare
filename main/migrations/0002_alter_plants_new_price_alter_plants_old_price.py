# Generated by Django 4.2.2 on 2023-06-19 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plants',
            name='new_price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='plants',
            name='old_price',
            field=models.FloatField(),
        ),
    ]