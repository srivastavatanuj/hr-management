# Generated by Django 5.1.3 on 2024-12-09 06:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplyLeaves',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leave_type', models.CharField(choices=[('SICK', 'Sick Leave'), ('CASUAL', 'Casual Leave'), ('PAID', 'Paid Leave'), ('MATERNITY', 'Maternity Leave'), ('FLEXI', 'Flexible Leave')], max_length=20)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('reason', models.TextField()),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('APPROVED', 'Approved'), ('REJECTED', 'Rejected')], default='PENDING', max_length=20)),
                ('approved_by_manager', models.BooleanField(default=False)),
                ('approved_by_hr', models.BooleanField(default=False)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applied_leaves', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmpLeaveBalance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sick', models.IntegerField(default=0)),
                ('casual', models.IntegerField(default=0)),
                ('paid', models.IntegerField(default=0)),
                ('maternity', models.IntegerField(default=0)),
                ('flexi', models.IntegerField(default=0)),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='leave_balance', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]