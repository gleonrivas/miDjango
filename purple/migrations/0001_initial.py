# Generated by Django 4.0.4 on 2022-05-13 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('img', models.TextField()),
                ('nombre', models.TextField()),
                ('autor', models.TextField()),
                ('fecha_publicacion', models.DateField()),
            ],
        ),
    ]
