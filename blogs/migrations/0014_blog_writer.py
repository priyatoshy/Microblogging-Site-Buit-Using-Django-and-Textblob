# Generated by Django 4.1.3 on 2022-11-22 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('blogs', '0013_alter_blog_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='writer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]
