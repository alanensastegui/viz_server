# Generated by Django 3.0.3 on 2020-02-04 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crimesapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crime',
            name='longitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='crime',
            name='time',
            field=models.DateTimeField(),
        ),
    ]
