# Generated by Django 5.0.3 on 2024-03-31 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mukofotlar", "0004_alter_prize_options_alter_prize_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="prize",
            name="name",
            field=models.CharField(max_length=200, verbose_name="prize name"),
        ),
    ]
