# Generated by Django 3.1.7 on 2021-04-16 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todotext',
            old_name='status',
            new_name='is_done',
        ),
    ]