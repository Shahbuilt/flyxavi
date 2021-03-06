# Generated by Django 3.1.7 on 2021-12-01 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flyxav', '0002_passport'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bankdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beneficiary_name', models.CharField(max_length=20, null=True)),
                ('beneficiary_address', models.CharField(max_length=20, null=True)),
                ('beneficiary_country', models.CharField(max_length=20, null=True)),
                ('beneficiary_bank', models.CharField(max_length=20, null=True)),
                ('beneficiary_acnumber', models.CharField(max_length=20, null=True)),
                ('beneficiary_baddress', models.CharField(max_length=20, null=True)),
                ('beneficiary_swiftcode', models.CharField(max_length=20, null=True)),
                ('beneficiary_iban', models.CharField(max_length=20, null=True)),
                ('beneficiary_sortcode', models.CharField(max_length=20, null=True)),
                ('beneficiary_bsb', models.CharField(max_length=20, null=True)),
                ('bank_details', models.FileField(upload_to='')),
            ],
        ),
    ]
