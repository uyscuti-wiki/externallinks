# Generated by Django 2.2 on 2019-06-03 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0003_auto_20190603_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisation',
            name='program',
            field=models.ManyToManyField(to='programs.Program'),
        ),
    ]
