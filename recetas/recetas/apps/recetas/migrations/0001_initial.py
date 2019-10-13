# Generated by Django 2.1.11 on 2019-10-13 02:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tipo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recetas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receta', models.CharField(max_length=5000000)),
                ('pasos', models.CharField(max_length=5000000)),
                ('ingredientes', models.CharField(max_length=5000000)),
                ('descripcion', models.CharField(max_length=5000000)),
                ('tipo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tipo.Descripcion')),
            ],
        ),
    ]
