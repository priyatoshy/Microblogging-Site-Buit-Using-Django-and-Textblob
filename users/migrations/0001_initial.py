# Generated by Django 4.1.3 on 2022-11-22 11:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('full_name', models.CharField(max_length=200)),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('phone_no', models.CharField(max_length=13)),
                ('address', models.TextField(blank=True, null=True)),
                ('profile_picture', models.ImageField(blank=True, default='profiles/default.png', null=True, upload_to='profiles/')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('user_role', models.CharField(blank=True, choices=[('PATIENT', 'PATIENT'), ('DOCTOR', 'DOCTOR'), ('NURSE', 'NURSE'), ('TECHNICIAN', 'TECHNICIAN'), ('STUFF', 'STUFF'), ('CLINIC ADMIN', 'CLINIC ADMIN')], default='PATIENT', max_length=255)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
