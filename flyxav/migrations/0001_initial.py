# Generated by Django 3.1.7 on 2021-11-27 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, null=True)),
                ('last_name', models.CharField(max_length=20, null=True)),
                ('picture', models.FileField(upload_to='')),
                ('location', models.CharField(max_length=20, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
