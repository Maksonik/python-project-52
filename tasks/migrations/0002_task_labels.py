# Generated by Django 5.1.4 on 2024-12-15 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0003_remove_label_tasks'),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='labels',
            field=models.ManyToManyField(blank=True, related_name='tasks', to='labels.label'),
        ),
    ]