# Generated by Django 4.0.1 

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
