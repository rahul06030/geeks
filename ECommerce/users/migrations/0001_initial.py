# Generated by Django 4.2.7 on 2023-11-24 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('middle_name', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_no', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('customer_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('is_disabled', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('additional_data', models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Authorization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('token', models.CharField(max_length=255)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.customer')),
            ],
        ),
    ]
