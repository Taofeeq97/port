# Generated by Django 4.2 on 2023-04-04 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(help_text='Enter full name', max_length=200)),
                ('title', models.CharField(help_text='Enter titles putting comma between them', max_length=200)),
                ('social_twitter', models.CharField(max_length=200)),
                ('social_facebook', models.CharField(max_length=200)),
                ('social_linkedin', models.CharField(max_length=200)),
                ('social_website', models.URLField()),
                ('phone_number', models.IntegerField()),
                ('email', models.EmailField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('project_completed', models.IntegerField(default=0)),
                ('happy_client', models.IntegerField(default=0)),
                ('years_of_experience', models.IntegerField(default=0)),
                ('hobby', models.CharField(blank=True, help_text='Enter hobbies putting commas in between them', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('progress_level', models.IntegerField(default=0)),
            ],
        ),
    ]
