# Generated by Django 3.0.6 on 2020-05-27 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0004_auto_20200526_1312'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location_track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('location', models.CharField(max_length=100)),
                ('ip', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms.Student')),
            ],
        ),
    ]
