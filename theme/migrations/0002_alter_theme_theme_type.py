# Generated by Django 4.1.4 on 2023-01-03 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("theme", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="theme",
            name="theme_type",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="theme_type",
                to="theme.themetype",
            ),
        ),
    ]
