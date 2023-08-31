# Generated by Django 4.2.4 on 2023-08-31 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=300)),
                ('phone', models.CharField(help_text='Enter a valid Mobile Number: ', max_length=15)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
