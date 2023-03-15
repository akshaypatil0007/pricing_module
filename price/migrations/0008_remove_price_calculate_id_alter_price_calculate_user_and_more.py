# Generated by Django 4.1.7 on 2023-03-15 03:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0007_alter_price_calculate_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='price_calculate',
            name='id',
        ),
        migrations.AlterField(
            model_name='price_calculate',
            name='user',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='trips',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='price.price_calculate'),
        ),
    ]