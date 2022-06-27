# Generated by Django 4.0.5 on 2022-06-27 20:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bav", "0005_customdocument"),
        ("home", "0003_standardpage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="standardpage",
            name="image",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="bav.customimage",
            ),
        ),
    ]
