# Generated by Django 5.1.1 on 2024-09-15 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_user_profile_created_by_profile_created_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='created_by',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='created',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='updated',
        ),
    ]
