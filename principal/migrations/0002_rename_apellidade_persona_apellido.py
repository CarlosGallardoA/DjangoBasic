# Generated by Django 3.2.6 on 2021-08-25 23:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='persona',
            old_name='apellidade',
            new_name='apellido',
        ),
    ]
