# Generated by Django 4.0.4 on 2022-05-13 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purple', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recomendado',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('img', models.TextField()),
                ('nombre', models.TextField()),
                ('autor', models.TextField()),
                ('fecha_publicacion', models.DateField()),
            ],
        ),
    ]
