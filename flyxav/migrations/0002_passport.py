# Generated by Django 3.1.7 on 2021-11-30 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flyxav', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passport_no', models.CharField(max_length=20, null=True)),
                ('passport_file', models.FileField(upload_to='')),
            ],
        ),
    ]
