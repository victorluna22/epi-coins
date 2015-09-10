# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='EpiUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('full_name', models.CharField(max_length=120, null=True, verbose_name='Nome', blank=True)),
                ('username', models.CharField(max_length=120, null=True, blank=True)),
                ('email', models.EmailField(null=True, max_length=254, blank=True, unique=True, verbose_name='Email', db_index=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designa se este usu\xe1rio pode acessar este site admin.', verbose_name='Membro da equipe')),
                ('is_active', models.BooleanField(default=True, help_text='Designa se este usu\xe1rio est\xe1 ativo.Desmarque esta op\xe7\xe3o ao inv\xe9s de deletar a conta.', verbose_name='Ativo')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'usu\xe1rio',
                'verbose_name_plural': 'usu\xe1rios',
            },
        ),
    ]
