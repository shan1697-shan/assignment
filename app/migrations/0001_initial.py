# Generated by Django 3.2.5 on 2021-07-25 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Devicedata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imei', models.CharField(max_length=10)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('cell1v', models.FloatField()),
                ('cell2v', models.FloatField()),
                ('cell3v', models.FloatField()),
                ('cell4v', models.FloatField()),
                ('cell5v', models.FloatField()),
                ('cell6v', models.FloatField()),
                ('cell7v', models.FloatField()),
                ('cell8v', models.FloatField()),
                ('cell9v', models.FloatField()),
                ('cell10v', models.FloatField()),
                ('cell11v', models.FloatField()),
                ('cell12v', models.FloatField()),
                ('cell13v', models.FloatField()),
                ('cell14v', models.FloatField()),
                ('avgv', models.FloatField()),
                ('packv', models.FloatField()),
                ('current', models.FloatField()),
                ('soc', models.IntegerField()),
            ],
        ),
    ]