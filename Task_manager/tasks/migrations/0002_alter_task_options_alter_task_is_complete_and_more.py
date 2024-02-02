# Generated by Django 4.2.9 on 2024-02-02 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-updated_at', '-created_at']},
        ),
        migrations.AlterField(
            model_name='task',
            name='is_complete',
            field=models.CharField(choices=[('Yes', 'yes'), ('No', 'no')], max_length=20),
        ),
        migrations.AlterField(
            model_name='task',
            name='photo',
            field=models.ImageField(default='', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('Low', 'low'), ('Medium', 'medium'), ('High', 'high')], max_length=20),
        ),
    ]