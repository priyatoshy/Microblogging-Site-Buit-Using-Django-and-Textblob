# Generated by Django 4.1.3 on 2022-11-22 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0014_blog_writer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='analysis',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
