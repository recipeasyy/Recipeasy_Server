# Generated by Django 4.1.4 on 2023-01-17 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0006_theme_save_count_theme_saved_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='image',
            field=models.URLField(default='https://www.example.com', max_length=2000),
            preserve_default=False,
        ),
    ]
