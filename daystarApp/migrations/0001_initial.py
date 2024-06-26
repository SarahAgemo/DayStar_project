# Generated by Django 5.0.4 on 2024-05-16 09:26

import daystarApp.models
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Baby',
            fields=[
                ('baby_id', models.AutoField(primary_key=True, serialize=False)),
                ('baby_name', models.CharField(max_length=20)),
                ('baby_gender', models.CharField(max_length=20)),
                ('date_of_birth', models.DateField(default=django.utils.timezone.now)),
                ('baby_location', models.CharField(max_length=20)),
                ('parents_name', models.CharField(max_length=20)),
                ('period_of_stay', models.CharField(choices=[('half-day', 'Half-day'), ('full-day', 'Full-day')], max_length=100)),
                ('registration_date', models.DateField(default=django.utils.timezone.now)),
                ('baby_bringer', models.CharField(max_length=20)),
                ('time_in', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Doll',
            fields=[
                ('doll_id', models.AutoField(primary_key=True, serialize=False)),
                ('doll_type', models.CharField(choices=[('birds', 'Birds'), ('animals', 'Animals'), ('vehicles', 'Vehicles'), ('human', 'Human'), ('other', 'Other')], max_length=20)),
                ('doll_name', models.CharField(max_length=20)),
                ('doll_price', models.IntegerField(blank=True, default=0, null=True)),
                ('doll_description', models.TextField(blank=True, max_length=30, null=True)),
                ('doll_quantity', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sitter_arrival',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sitter_number', models.IntegerField(default=0)),
                ('date_of_arrival', models.DateField(default=django.utils.timezone.now)),
                ('timein', models.TimeField()),
                ('Attendancestatus', models.CharField(choices=[('On-duty', 'On-duty')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sitterform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=100)),
                ('location', models.CharField(choices=[('kabalagala', 'kabalagala')], max_length=100)),
                ('date_of_birth', models.DateField(default=django.utils.timezone.now)),
                ('next_of_kin', models.CharField(max_length=200)),
                ('national_identification_number', models.CharField(max_length=200, validators=[daystarApp.models.NIN])),
                ('recommenders_name', models.CharField(max_length=200)),
                ('religon', models.CharField(blank=True, max_length=200, null=True)),
                ('level_of_education', models.CharField(choices=[('degree', 'Degree'), ('diploma', 'Diploma'), ('highschool certificate', 'Highschool certificate'), ('others', 'Others')], max_length=200)),
                ('sitter_number', models.IntegerField(default=0)),
                ('contacts', models.CharField(max_length=200, validators=[daystarApp.models.contacts])),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('stock_id', models.AutoField(primary_key=True, serialize=False)),
                ('stock_type', models.CharField(choices=[('milk', 'Milk'), ('diapers', 'Diapers'), ('fruits', 'Fruits'), ('wipes', 'Wipes'), ('other', 'Other')], max_length=200)),
                ('stock_name', models.CharField(max_length=200)),
                ('stock_price', models.IntegerField(default=0)),
                ('stock_quantity', models.IntegerField(default=0)),
                ('stock_description', models.TextField(blank=True, max_length=30, null=True)),
                ('date_stocked', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='BabyDeparture',
            fields=[
                ('baby_id', models.AutoField(primary_key=True, serialize=False)),
                ('baby_picker', models.CharField(max_length=20)),
                ('date_of_departure', models.DateField(default=django.utils.timezone.now)),
                ('time_out', models.TimeField()),
                ('comment', models.TextField(blank=True, null=True)),
                ('name_of_baby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='daystarApp.baby')),
            ],
        ),
        migrations.CreateModel(
            name='BabyPayment',
            fields=[
                ('baby_id', models.AutoField(primary_key=True, serialize=False)),
                ('period_of_stay', models.CharField(choices=[('half-day', 'Half-day'), ('full-day', 'Full-day'), ('monthly-halfday', 'Monthly-halfday'), ('monthly-fullday', 'Monthly-fullday')], max_length=100)),
                ('amount_paid', models.IntegerField(default=0)),
                ('original_amount', models.IntegerField(default=0)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('parent_name', models.CharField(max_length=20)),
                ('amount_due', models.IntegerField(default=0)),
                ('name_of_baby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='daystarApp.baby')),
            ],
        ),
        migrations.CreateModel(
            name='Doll_payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doll_type', models.CharField(choices=[('birds', 'Birds'), ('animals', 'Animals'), ('vehicles', 'Vehicles'), ('human', 'Human'), ('other', 'Other')], max_length=20)),
                ('amount_paid', models.IntegerField(default=0)),
                ('doll_price', models.IntegerField(blank=True, default=0, null=True)),
                ('doll_quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('parents_name', models.CharField(max_length=20)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('amount_due', models.IntegerField(default=0)),
                ('babe_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='daystarApp.baby')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='daystarApp.doll')),
            ],
        ),
        migrations.AddField(
            model_name='baby',
            name='Assigned_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='daystarApp.sitter_arrival'),
        ),
        migrations.CreateModel(
            name='Sitter_departure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sitter_number', models.IntegerField(default=0)),
                ('date_of_departure', models.DateField(default=django.utils.timezone.now)),
                ('timeout', models.TimeField()),
                ('Attendancestatus', models.CharField(choices=[('offduty', 'offduty')], max_length=100)),
                ('sitter_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='daystarApp.sitter_arrival')),
            ],
        ),
        migrations.CreateModel(
            name='Sitter_payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=3000)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('no_of_babies', models.IntegerField(default=0)),
                ('sitter_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='daystarApp.sitter_arrival')),
            ],
        ),
        migrations.AddField(
            model_name='sitter_arrival',
            name='sitter_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='daystarApp.sitterform'),
        ),
        migrations.CreateModel(
            name='Stock_issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_type', models.CharField(choices=[('milk', 'Milk'), ('diapers', 'Diapers'), ('fruits', 'Fruits'), ('wipes', 'Wipes')], max_length=200)),
                ('stock_quantity', models.IntegerField(default=0)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('comment', models.TextField(blank=True, null=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='daystarApp.stock')),
            ],
        ),
    ]
