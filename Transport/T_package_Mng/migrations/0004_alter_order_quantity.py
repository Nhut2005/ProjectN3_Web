# Generated by Django 5.1.4 on 2025-01-09 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('T_package_Mng', '0003_customer_active_employee_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]