# Generated by Django 4.0.5 on 2022-06-14 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bav", "0002_customimage_rendition"),
    ]

    operations = [
        migrations.AddField(
            model_name="customimage",
            name="malicious",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="customimage",
            name="sanned",
            field=models.BooleanField(default=False),
        ),
    ]
