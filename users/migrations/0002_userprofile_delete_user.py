# Generated by Django 4.2.3 on 2024-03-06 22:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brain_injury_details', models.TextField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('goal', models.CharField(blank=True, choices=[('improve_mental_health', 'Improve Mental Health'), ('enhance_cognitive_function', 'Enhance Cognitive Function'), ('promote_physical_wellness', 'Promote Physical Wellness'), ('facilitate_emotional_recovery', 'Facilitate Emotional Recovery'), ('support_social_integration', 'Support Social Integration')], max_length=50)),
                ('determination_level', models.CharField(blank=True, choices=[('casual', 'Casual'), ('determined', 'Determined'), ('very_determined', 'Very Determined')], max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]