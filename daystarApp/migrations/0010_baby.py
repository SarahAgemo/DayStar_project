# Generated by Django 5.0.4 on 2024-04-27 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daystarApp', '0009_alter_forgot_pass_email_alter_sign_in_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Baby',
            fields=[
                ('baby_id', models.AutoField(primary_key=True, serialize=False)),
                ('baby_name', models.CharField(blank=True, max_length=20, null=True)),
                ('baby_gender', models.CharField(blank=True, max_length=20, null=True)),
                ('baby_age', models.IntegerField(blank=True, null=True)),
                ('baby_locattion', models.CharField(blank=True, max_length=20, null=True)),
                ('baby_bringer', models.CharField(blank=True, max_length=20, null=True)),
                ('baby_arrivaltime', models.DateTimeField(blank=True, null=True)),
                ('parents_name', models.CharField(blank=True, max_length=20)),
                ('period_of_stay', models.DateTimeField(blank=True, null=True)),
                ('baby_fee', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]
