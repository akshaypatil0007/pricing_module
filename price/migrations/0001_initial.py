# Generated by Django 4.1.7 on 2023-03-04 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Price_Calculate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Distance_Base_Price', models.CharField(max_length=10)),
                ('Distance_travel', models.CharField(max_length=10)),
                ('Distance_Additional_Price', models.CharField(max_length=10)),
                ('Time_in_hours', models.CharField(max_length=5)),
                ('final_price', models.CharField(max_length=10)),
            ],
        ),
    ]