# Generated by Django 4.2.6 on 2023-12-08 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0002_alter_thing_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thing',
            name='description',
            field=models.TextField(blank=True, max_length=119),
        ),
    ]