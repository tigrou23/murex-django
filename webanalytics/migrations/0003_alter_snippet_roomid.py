# Generated by Django 4.1.4 on 2022-12-23 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "webanalytics",
            "0002_rename_language_snippet_roomid_remove_snippet_code_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="snippet", name="roomid", field=models.TextField(),
        ),
    ]