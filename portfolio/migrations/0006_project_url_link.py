# Generated by Django 4.2 on 2023-04-06 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_alter_profile_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='url_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
