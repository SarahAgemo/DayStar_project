# Generated by Django 5.0.4 on 2024-04-22 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('daystarApp', '0005_alter_forgot_pass_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='forgot_pass',
            old_name='email',
            new_name='email2',
        ),
        migrations.RenameField(
            model_name='sign_up',
            old_name='email',
            new_name='email1',
        ),
    ]
