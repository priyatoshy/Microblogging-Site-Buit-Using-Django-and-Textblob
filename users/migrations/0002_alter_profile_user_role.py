# Generated by Django 4.1.3 on 2022-11-22 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_role',
            field=models.CharField(blank=True, choices=[('BLOGGER', 'BLOGGER')], default='BLOGGER', max_length=255),
        ),
    ]
