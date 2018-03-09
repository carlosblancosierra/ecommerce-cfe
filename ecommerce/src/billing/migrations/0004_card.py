# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-09 20:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0003_billingprofile_customer_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_id', models.CharField(max_length=120)),
                ('brand', models.CharField(blank=True, max_length=120, null=True)),
                ('country', models.CharField(blank=True, max_length=120, null=True)),
                ('exp_month', models.IntegerField()),
                ('exp_year', models.IntegerField()),
                ('last4', models.CharField(blank=True, max_length=4, null=True)),
                ('billing_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.BillingProfile')),
            ],
        ),
    ]
