# Generated by Django 4.1.3 on 2022-11-25 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0021_comment_likes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ('-rate',)},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-likes',)},
        ),
    ]
