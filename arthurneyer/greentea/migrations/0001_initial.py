# Generated by Django 3.2 on 2021-05-12 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArtisticIp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lay_a', models.CharField(max_length=3)),
                ('lay_b', models.CharField(max_length=3)),
                ('lay_c', models.CharField(max_length=3)),
                ('lay_d', models.CharField(max_length=3)),
            ],
        ),
    ]
