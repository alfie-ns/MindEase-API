# Generated by Django 4.2.3 on 2024-03-17 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_userprofile_brain_injury_severity_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='brain_injury_type',
            new_name='brain_injury_context',
        ),
    ]