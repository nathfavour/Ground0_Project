# Generated by Django 4.0.6 on 2023-03-02 00:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Nathaniel', '0003_alter_employee_id_alter_employee_written'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='written',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 2, 0, 22, 20, 232167, tzinfo=utc)),
        ),
    ]
