# Generated by Django 4.1.7 on 2023-03-04 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0004_remove_price_calculate_final_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price_calculate',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]