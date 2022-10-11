# Generated by Django 4.0.5 on 2022-10-11 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='imgs')),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent_price', models.IntegerField(default=0)),
                ('house_size', models.TextField(max_length=500)),
                ('location', models.TextField(max_length=500)),
                ('bedroom', models.IntegerField(default=0)),
                ('bathroom', models.IntegerField(default=0)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.img')),
            ],
        ),
    ]