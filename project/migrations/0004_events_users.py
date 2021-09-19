# Generated by Django 3.2.7 on 2021-09-19 00:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0003_events_isvirtual'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='users',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='auth.user'),
            preserve_default=False,
        ),
    ]