# Generated by Django 2.2.3 on 2019-08-12 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_thing_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='thing',
            name='public',
            field=models.BooleanField(default=False),
        ),
    ]
