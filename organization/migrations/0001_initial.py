# Generated by Django 5.1.3 on 2024-12-09 06:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('domain', models.CharField(max_length=100, unique=True)),
                ('registration_number', models.CharField(blank=True, max_length=50, unique=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='org_logos')),
                ('industry_type', models.CharField(max_length=100)),
                ('website', models.CharField(blank=True, max_length=100, unique=True)),
                ('contact_email', models.EmailField(max_length=254)),
                ('contact_phone', models.CharField(max_length=20)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('subscription_plan', models.CharField(choices=[('basic', 'basic'), ('pro', 'pro'), ('enterprise', 'enterprise')], default='basic', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='NoticeBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('time', models.DateTimeField(auto_now=True)),
                ('priority', models.CharField(choices=[('low', 'low'), ('mid', 'mid'), ('high', 'high')], max_length=100)),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notice', to='organization.organization')),
            ],
        ),
        migrations.CreateModel(
            name='LeavePolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leave_type', models.CharField(choices=[('sick', 'Sick Leave'), ('casual', 'Casual Leave'), ('paid', 'Paid Leave'), ('maternity', 'Maternity Leave'), ('flexi', 'Flexi Leave')], max_length=50)),
                ('max_days', models.PositiveIntegerField()),
                ('carry_forward', models.BooleanField(default=False)),
                ('applicable_from', models.DateField()),
                ('applicable_to', models.DateField()),
                ('leaves_per_month', models.FloatField()),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leaves', to='organization.organization')),
            ],
        ),
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('flexi', models.BooleanField(default=False)),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='holiday', to='organization.organization')),
            ],
        ),
    ]