# Generated by Django 4.0.1 on 2022-02-03 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='header',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='replytocomment',
            name='header',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]