# Generated by Django 3.1.5 on 2022-05-29 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippetsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flower',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('flowername', models.CharField(max_length=30)),
                ('flowercolor', models.CharField(max_length=20)),
                ('isSingle', models.BooleanField(default=True)),
            ],
        ),
    ]
