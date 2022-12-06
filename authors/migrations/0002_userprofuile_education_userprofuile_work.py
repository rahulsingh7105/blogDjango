
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofuile',
            name='education',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='userprofuile',
            name='work',
            field=models.TextField(blank=True),
        ),
    ]
