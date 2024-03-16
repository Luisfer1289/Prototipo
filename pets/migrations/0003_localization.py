# Generated by Django 4.2.6 on 2024-02-13 20:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pets', '0002_alter_pet_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Localization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion_ip', models.GenericIPAddressField()),
                ('latitud', models.FloatField()),
                ('longitud', models.FloatField()),
                ('calle', models.CharField(max_length=255)),
                ('ciudad', models.CharField(max_length=255)),
                ('estado', models.CharField(max_length=255)),
                ('pais', models.CharField(max_length=255)),
                ('hora', models.DateTimeField(auto_now_add=True)),
                ('mascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pets.pet')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]