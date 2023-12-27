# Generated by Django 4.2.5 on 2023-12-04 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebWater', '0002_products_type_bottle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='type_bottle',
            field=models.CharField(choices=[('largeBottleOfWater', 'Вода питьевая 5 л - 19 л'), ('bottleOfWater', 'Вода питьевая 1,5 л'), ('middleBottleOfWater', 'Вода питьевая 0,5 л'), ('sweetBottleOfWater', 'Напитки')], default='Other', max_length=30, verbose_name='Класс продукта'),
        ),
    ]
