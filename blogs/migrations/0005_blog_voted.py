# Generated by Django 4.1.3 on 2022-11-03 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_alter_blog_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='voted',
            field=models.IntegerField(default=0),
        ),
    ]