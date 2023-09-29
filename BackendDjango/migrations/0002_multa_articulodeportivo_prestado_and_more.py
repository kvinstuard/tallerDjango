# Generated by Django 4.2.5 on 2023-09-29 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BackendDjango', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Multa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.IntegerField()),
                ('fechaPago', models.DateTimeField()),
                ('pagado', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='articulodeportivo',
            name='prestado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='univallunos',
            name='tieneArticulo',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='articulodeportivo',
            name='valor',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='univallunos',
            name='codigoEstudiante',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='univallunos',
            name='numeroDocumento',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='Prestamos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaEntrega', models.DateTimeField()),
                ('articulo', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='BackendDjango.articulodeportivo')),
                ('univalluno', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='BackendDjango.univallunos')),
            ],
        ),
    ]
