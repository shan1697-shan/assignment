# Generated by Django 3.2.5 on 2021-07-25 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='devicedata',
            name='created_on',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='devicedata',
            name='datavia',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]