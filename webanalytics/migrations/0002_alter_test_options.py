# Generated by Django 4.1.5 on 2023-01-30 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("webanalytics", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="test",
            options={"ordering": ["-date"]},
        ),
    ]