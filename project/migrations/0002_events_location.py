# Generated by Django 3.2.7 on 2021-09-19 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_events'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='location',
            field=models.CharField(default='0', max_length=50),
            preserve_default=False,
        ),
    ]