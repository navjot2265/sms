# Generated by Django 3.0.6 on 2020-05-26 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0002_auto_20200525_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(default='1234', max_length=10),
        ),
        migrations.AddField(
            model_name='student',
            name='rollno',
            field=models.IntegerField(default=100),
        ),
    ]
