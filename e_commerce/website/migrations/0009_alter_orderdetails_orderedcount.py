# Generated by Django 4.2.4 on 2023-09-06 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_order_totalprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetails',
            name='orderedCount',
            field=models.IntegerField(null=True),
        ),
    ]