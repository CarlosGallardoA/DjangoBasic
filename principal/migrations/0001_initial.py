# Generated by Django 3.2.6 on 2021-08-25 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=120)),
                ('apellidade', models.CharField(max_length=120)),
                ('correo', models.EmailField(max_length=200)),
            ],
        ),
    ]
