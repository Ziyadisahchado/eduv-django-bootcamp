# Generated by Django 3.2.8 on 2021-10-30 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0017_alter_job_confirmed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
