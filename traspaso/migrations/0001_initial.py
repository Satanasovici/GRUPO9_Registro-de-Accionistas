# Generated by Django 2.2.7 on 2019-11-26 01:47

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accionista', '0001_initial'),
        ('tercero', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acciones',
            fields=[
                ('acciones_id', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=20)),
                ('tipo', models.CharField(default='', max_length=20)),
                ('serie', models.CharField(default='', max_length=20)),
                ('cantidad', models.IntegerField(default='')),
                ('estado', models.CharField(default='', max_length=20)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('accionista_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accionista.Accionista')),
                ('tercero_id', models.ManyToManyField(blank=True, to='tercero.Tercero')),
            ],
            managers=[
                ('acciones', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Traspaso',
            fields=[
                ('traspaso_id', models.AutoField(primary_key=True, serialize=False)),
                ('run_venta', models.CharField(max_length=20)),
                ('run_compra', models.CharField(max_length=20)),
                ('estado', models.CharField(choices=[('espera', 'ESPERA'), ('aprobado', 'APROBADO'), ('rechazado', 'RECHAZADO')], default='', max_length=200)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('acciones_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='traspaso.Acciones')),
            ],
            managers=[
                ('traspasos', django.db.models.manager.Manager()),
            ],
        ),
    ]
