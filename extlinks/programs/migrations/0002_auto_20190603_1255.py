# Generated by Django 2.2 on 2019-06-03 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='program',
            options={'ordering': ['name']},
        ),
    ]
