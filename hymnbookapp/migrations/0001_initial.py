# Generated by Django 4.0.1 on 2022-01-21 13:02

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Approved_Sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sector_name', models.CharField(db_index=True, max_length=200, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Investor',
            fields=[
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=200, null=True)),
                ('program_title', models.CharField(max_length=200)),
                ('program_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('amount_invested', models.DecimalField(decimal_places=2, default=0, max_digits=30)),
                ('amount_left', models.DecimalField(decimal_places=2, default=0, max_digits=30)),
                ('targeted_startup_number', models.IntegerField(default=0)),
                ('program_start', models.DateTimeField()),
                ('program_ends', models.DateTimeField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('startup_name', models.CharField(max_length=250, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('account_type', models.CharField(choices=[('Investor', 'Investor'), ('Startup', 'StartUp')], max_length=13)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('startup_sector', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hymnbookapp.approved_sector')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Startup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initial_amount_requested', models.DecimalField(decimal_places=2, default=0, max_digits=30)),
                ('amount_given', models.DecimalField(decimal_places=2, default=0, max_digits=30)),
                ('description_purpose_of_request', models.TextField(blank=True, null=True)),
                ('startup_status', models.CharField(choices=[('Accepted', 'Accepted'), ('Rejected', 'Rejected')], max_length=13)),
                ('date_founded', models.DateTimeField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('investor_programs', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hymnbookapp.investor')),
                ('startup_profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hymnbookapp.profile')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.AddField(
            model_name='investor',
            name='investor_profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='investorprofile', to='hymnbookapp.profile'),
        ),
        migrations.AddField(
            model_name='investor',
            name='sectors',
            field=models.ManyToManyField(related_name='sectors', to='hymnbookapp.Approved_Sector'),
        ),
    ]
