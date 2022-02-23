# Generated by Django 4.0.1 on 2022-02-18 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hymnbookapp', '0004_snippet'),
    ]

    operations = [
        migrations.CreateModel(
            name='profession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=200)),
                ('salary', models.CharField(max_length=200)),
                ('job_note', models.TextField()),
                ('level', models.CharField(choices=[('L1', 'L1'), ('L2', 'L2'), ('L3', 'L3'), ('Others', 'Others')], max_length=13)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=13)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=50, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('jobs', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hymnbookapp.profession')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]