# Generated by Django 4.2.3 on 2023-07-18 17:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0005_recipe_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2023, 7, 18, 19, 32, 33, 613149), unique=True),
            preserve_default=False,
        ),
    ]
