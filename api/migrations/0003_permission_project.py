# Generated by Django 4.2 on 2023-04-13 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_user_task_assign_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='permission',
            name='project',
            field=models.ForeignKey(default=789654, on_delete=django.db.models.deletion.CASCADE, to='api.project'),
        ),
    ]
