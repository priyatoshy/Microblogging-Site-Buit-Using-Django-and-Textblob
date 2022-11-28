# Generated by Django 4.1.3 on 2022-11-03 06:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='rate',
            field=models.CharField(blank=True, choices=[('💓', 'Love'), ('💙', 'LIKE'), ('💔', 'DISLIKE')], max_length=255),
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(blank=True, to='blogs.tags'),
        ),
    ]
