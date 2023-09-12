# Generated by Django 4.2.4 on 2023-09-12 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_alter_order_customer_alter_productimages_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Declined', 'Declined'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered')], max_length=100),
        ),
        migrations.AlterField(
            model_name='productimages',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.product'),
        ),
    ]