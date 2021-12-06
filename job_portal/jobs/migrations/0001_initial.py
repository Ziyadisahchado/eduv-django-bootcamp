# Generated by Django 3.2.9 on 2021-12-05 21:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0009_confirmation_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=300)),
                ('application_email', models.EmailField(max_length=254)),
                ('appliction_url', models.URLField()),
                ('salary', models.IntegerField(blank=True)),
                ('description', models.TextField()),
                ('education_experience', models.TextField()),
                ('requirements', models.TextField()),
                ('slots', models.IntegerField()),
                ('job_nature', models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time')], max_length=200)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='jobs.category')),
                ('posted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.recruiter')),
            ],
        ),
    ]
