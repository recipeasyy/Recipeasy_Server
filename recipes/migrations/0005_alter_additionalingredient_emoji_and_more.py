# Generated by Django 4.1.4 on 2022-12-30 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_remove_additionalingredient_imoji_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionalingredient',
            name='emoji',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='requiredingredient',
            name='emoji',
            field=models.CharField(default='temp', max_length=50),
            preserve_default=False,
        ),
    ]
