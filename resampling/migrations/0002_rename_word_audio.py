# Generated by Django 4.1.3 on 2022-11-03 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("resampling", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Word",
            new_name="Audio",
        ),
    ]
