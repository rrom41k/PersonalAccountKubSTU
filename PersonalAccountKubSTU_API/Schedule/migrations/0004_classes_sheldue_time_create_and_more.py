# Generated by Django 4.2.7 on 2023-12-02 21:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Schedule', '0003_alter_specialization_number_specialization'),
    ]

    operations = [
        migrations.AddField(
            model_name='classes_sheldue',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='classes_sheldue',
            name='time_update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]