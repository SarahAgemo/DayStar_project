# Generated by Django 5.0.4 on 2024-05-15 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daystarApp', '0007_babypayment_amount_due_babypayment_parent_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sign_in',
            name='email',
            field=models.EmailField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='sign_in',
            name='password',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='sign_up',
            name='email',
            field=models.EmailField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='sign_up',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='sign_up',
            name='password',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='sign_up',
            name='phone',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sign_up',
            name='repeat_password',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
