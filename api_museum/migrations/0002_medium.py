# Generated by Django 4.0.5 on 2022-06-23 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_museum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medium',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=200)),
                ('status', models.BooleanField()),
            ],
        ),
    ]
