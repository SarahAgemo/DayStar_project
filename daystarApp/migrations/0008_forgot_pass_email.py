# Generated by Django 5.0.4 on 2024-04-22 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daystarApp', '0007_remove_forgot_pass_email2_remove_sign_up_email1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='forgot_pass',
            name='email',
            field=models.EmailField(blank=True, max_length=20, null=True),
        ),
    ]
