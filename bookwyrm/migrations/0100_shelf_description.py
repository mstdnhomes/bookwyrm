# Generated by Django 3.2.5 on 2021-09-28 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookwyrm", "0099_readthrough_is_active"),
    ]

    operations = [
        migrations.AddField(
            model_name="shelf",
            name="description",
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]