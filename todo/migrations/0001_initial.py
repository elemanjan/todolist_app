# Generated by Django 3.1.7 on 2021-04-16 10:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TodoText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата создания')),
                ('due', models.DateField(blank=True, null=True, verbose_name='Дата выполнения')),
                ('status', models.BooleanField(default=False, null=True, verbose_name='Статус выполнения')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
