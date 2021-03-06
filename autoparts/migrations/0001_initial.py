# Generated by Django 3.0.8 on 2020-12-15 23:01

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='AVDevices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_antennaassembly', models.IntegerField(null=True)),
                ('price_radioplayer', models.IntegerField(null=True)),
                ('price_speaker', models.IntegerField(null=True)),
                ('price_tuner', models.IntegerField(null=True)),
                ('price_subwoofer', models.IntegerField(null=True)),
                ('price_videoplayer', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Body',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_bonnet', models.IntegerField(null=True)),
                ('price_bumper', models.IntegerField(null=True)),
                ('price_cowl', models.IntegerField(null=True)),
                ('price_decklid', models.IntegerField(null=True)),
                ('price_fascia', models.IntegerField(null=True)),
                ('price_fender', models.IntegerField(null=True)),
                ('price_frontclip', models.IntegerField(null=True)),
                ('price_frontfascia', models.IntegerField(null=True)),
                ('price_grille', models.IntegerField(null=True)),
                ('price_pillar', models.IntegerField(null=True)),
                ('price_quarterpanel', models.IntegerField(null=True)),
                ('price_radiator', models.IntegerField(null=True)),
                ('price_rocker', models.IntegerField(null=True)),
                ('price_roofrack', models.IntegerField(null=True)),
                ('price_spoiler', models.IntegerField(null=True)),
                ('price_rims', models.IntegerField(null=True)),
                ('price_trimpackage', models.IntegerField(null=True)),
                ('price_trunk', models.IntegerField(null=True)),
                ('price_valance', models.IntegerField(null=True)),
                ('price_weldedassembly', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cameras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_backupcamera', models.IntegerField(null=True)),
                ('price_dashcam', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Doors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_antiintrusionbar', models.IntegerField(null=True)),
                ('price_outerdoorhandle', models.IntegerField(null=True)),
                ('price_innerdoorhandle', models.IntegerField(null=True)),
                ('price_windowmotor', models.IntegerField(null=True)),
                ('price_doorcontrolmodule', models.IntegerField(null=True)),
                ('price_doorseal', models.IntegerField(null=True)),
                ('price_doorwatershield', models.IntegerField(null=True)),
                ('price_hinge', models.IntegerField(null=True)),
                ('price_doorlatch', models.IntegerField(null=True)),
                ('price_doorlock', models.IntegerField(null=True)),
                ('price_centrallocking', models.IntegerField(null=True)),
                ('price_fueltankdoor', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Windows',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_glass', models.IntegerField(null=True)),
                ('price_sunroof', models.IntegerField(null=True)),
                ('price_sunroofrail', models.IntegerField(null=True)),
                ('price_sunroofglass', models.IntegerField(null=True)),
                ('price_windowmotor', models.IntegerField(null=True)),
                ('price_windowregulator', models.IntegerField(null=True)),
                ('price_windshield', models.IntegerField(null=True)),
                ('price_windowseal', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
