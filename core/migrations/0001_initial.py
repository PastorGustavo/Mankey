# Generated by Django 4.0.4 on 2022-05-25 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=9999)),
                ('img', models.ImageField(upload_to='')),
                ('nome', models.CharField(max_length=300)),
                ('preco', models.IntegerField()),
            ],
        ),
    ]