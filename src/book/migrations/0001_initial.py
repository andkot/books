# Generated by Django 3.1.1 on 2020-09-30 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('author_name', models.CharField(max_length=255, verbose_name='Author name')),
                ('description', models.TextField(verbose_name='Description')),
            ],
        ),
    ]
