# Generated by Django 4.0.4 on 2022-08-24 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=255)),
                ('client_org', models.CharField(max_length=255)),
                ('bill_num', models.IntegerField()),
                ('bill_sum', models.FloatField()),
                ('date', models.DateField(verbose_name='%d-%m-%Y')),
                ('service', models.TextField()),
            ],
        ),
    ]
