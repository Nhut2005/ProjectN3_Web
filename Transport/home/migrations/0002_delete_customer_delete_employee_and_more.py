# Generated by Django 5.1.4 on 2025-01-09 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='inforTransport',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]