# Generated by Django 4.2.5 on 2023-09-29 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BackendDjango', '0003_alter_prestamos_articulo_alter_prestamos_univalluno_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamos',
            name='articulo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='BackendDjango.articulodeportivo'),
        ),
        migrations.AlterField(
            model_name='prestamos',
            name='univalluno',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='BackendDjango.univallunos'),
        ),
    ]