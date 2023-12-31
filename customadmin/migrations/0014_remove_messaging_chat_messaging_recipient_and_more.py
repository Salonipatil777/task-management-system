# Generated by Django 4.2.2 on 2023-07-05 07:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customadmin', '0013_alter_employee_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messaging',
            name='chat',
        ),
        migrations.AddField(
            model_name='messaging',
            name='recipient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='messaging',
            name='sender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to=settings.AUTH_USER_MODEL),
        ),
    ]
