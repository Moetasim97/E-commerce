# Generated by Django 4.2.4 on 2023-09-12 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_alter_order_status_alter_productimages_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
