# Generated by Django 5.1.1 on 2024-10-06 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('species', models.CharField(max_length=50)),
                ('breed', models.CharField(max_length=50)),
                ('age', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('available', models.BooleanField(default=True)),
            ],
        ),
    ]
