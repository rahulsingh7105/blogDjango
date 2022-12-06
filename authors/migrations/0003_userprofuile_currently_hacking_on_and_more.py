
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0002_userprofuile_education_userprofuile_work'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofuile',
            name='currently_hacking_on',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='userprofuile',
            name='currently_learning',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='userprofuile',
            name='skills_language',
            field=models.TextField(blank=True),
        ),
    ]
