# Generated by Django 5.1.4 on 2025-01-09 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('T_package_Mng', '0004_alter_order_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.CharField(max_length=255),
        ),
    ]
