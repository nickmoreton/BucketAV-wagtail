# Generated by Django 4.0.5 on 2022-06-16 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bav", "0003_customimage_malicious_customimage_sanned"),
    ]

    operations = [
        migrations.DeleteModel(
            name="BavItem",
        ),
        migrations.RenameField(
            model_name="customimage",
            old_name="sanned",
            new_name="scanned",
        ),
    ]
