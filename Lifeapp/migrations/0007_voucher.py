# Generated by Django 4.2.8 on 2024-01-06 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lifeapp', '0006_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=255)),
                ('amount', models.CharField(max_length=255)),
                ('pay', models.CharField(max_length=50)),
                ('auth', models.CharField(max_length=50)),
                ('approve', models.CharField(max_length=50)),
            ],
        ),
    ]