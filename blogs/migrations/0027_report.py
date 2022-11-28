# Generated by Django 4.1.3 on 2022-11-28 06:12

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_profile_bio'),
        ('blogs', '0026_alter_blog_featured_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('report', models.TextField(max_length=50)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('blog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blogs.blog')),
                ('reported_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
            options={
                'ordering': ('-created_on',),
                'unique_together': {('blog', 'reported_by')},
            },
        ),
    ]
