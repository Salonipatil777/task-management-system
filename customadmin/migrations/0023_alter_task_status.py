# Generated by Django 4.2.2 on 2023-07-10 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customadmin', '0022_alter_employee_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
