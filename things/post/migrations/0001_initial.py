# Generated by Django 2.2.3 on 2019-07-29 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Thing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(default=' ', max_length=2048)),
                ('added_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
