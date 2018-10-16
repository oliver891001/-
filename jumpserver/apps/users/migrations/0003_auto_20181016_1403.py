# Generated by Django 2.1 on 2018-10-16 06:03

import common.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20171225_1157'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['username'], 'verbose_name': 'User'},
        ),
        migrations.AlterModelOptions(
            name='usergroup',
            options={'ordering': ['name'], 'verbose_name': 'User group'},
        ),
        migrations.RemoveField(
            model_name='user',
            name='enable_otp',
        ),
        migrations.RemoveField(
            model_name='user',
            name='secret_key_otp',
        ),
        migrations.AddField(
            model_name='loginlog',
            name='mfa',
            field=models.SmallIntegerField(choices=[(0, 'Disabled'), (1, 'Enabled'), (2, '-')], default=2, verbose_name='MFA'),
        ),
        migrations.AddField(
            model_name='loginlog',
            name='reason',
            field=models.SmallIntegerField(choices=[(0, '-'), (1, 'Username/password check failed'), (2, 'MFA authentication failed')], default=0, verbose_name='Reason'),
        ),
        migrations.AddField(
            model_name='loginlog',
            name='status',
            field=models.BooleanField(choices=[(True, 'Success'), (False, 'Failed')], default=True, max_length=2, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='user',
            name='_otp_secret_key',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='otp_level',
            field=models.SmallIntegerField(choices=[(0, 'Disable'), (1, 'Enable'), (2, 'Force enable')], default=0, verbose_name='MFA'),
        ),
        migrations.AddField(
            model_name='user',
            name='source',
            field=models.CharField(choices=[('local', 'Local'), ('ldap', 'LDAP/AD')], default='local', max_length=30, verbose_name='Source'),
        ),
        migrations.AddField(
            model_name='usergroup',
            name='org_id',
            field=models.CharField(blank=True, default='', max_length=36, verbose_name='Organization'),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_expired',
            field=models.DateTimeField(blank=True, db_index=True, default=common.utils.date_expired_default, null=True, verbose_name='Date expired'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_first_login',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='usergroup',
            name='created_by',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.RemoveField(
            model_name='usergroup',
            name='discard_time',
        ),
        migrations.RemoveField(
            model_name='usergroup',
            name='is_discard',
        ),
        migrations.AlterUniqueTogether(
            name='usergroup',
            unique_together={('org_id', 'name')},
        ),
    ]
