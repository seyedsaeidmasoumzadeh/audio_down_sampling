# Generated by Django 4.1.3 on 2022-11-03 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("resampling", "0002_rename_word_audio"),
    ]

    operations = [
        migrations.RenameField(
            model_name="audio",
            old_name="audio_file_name",
            new_name="audio_name",
        ),
        migrations.AlterField(
            model_name="audio",
            name="audio_file",
            field=models.FileField(upload_to="audio"),
        ),
    ]
