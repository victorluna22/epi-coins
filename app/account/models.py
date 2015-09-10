#encoding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import User

class EpiUserManager(BaseUserManager):
    def _create_user(self, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        now = timezone.now()

        if email:
            # raise ValueError(_(u'É necessário um email válido.'))
            email = self.normalize_email(email)
        user = self.model(email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, True, True,
                                 **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True,
                                 **extra_fields)

    def validate_hash_activate(self, hash):
        try:
            string = base64.b64decode(hash)
            id, email = string.split('!@#')
            if self.filter(id=id, email=email).exists():
                return self.get(id=id)
            return None
        except:
            return None

class EpiUser(AbstractBaseUser, PermissionsMixin):
    """
    A fully featured User model with admin-compliant permissions that uses
    a full-length email field as the username.

    Email and password are required. Other fields are optional.
    """
    # TODO: make full_name obligatory
    full_name = models.CharField(verbose_name=_(u'Nome'), max_length=120, blank=True, null=True)
    username = models.CharField(blank=True, null=True, max_length=120)
    email = models.EmailField(verbose_name=_(u'Email'), max_length=254, unique=True, db_index=True, null=True, blank=True)
    is_staff = models.BooleanField(verbose_name=_(u'Membro da equipe'), default=False,
                                   help_text=_(u'Designa se este usuário pode acessar este site admin.'))
    is_active = models.BooleanField(verbose_name=_(u'Ativo'), default=True,
                                    help_text=_(u'Designa se este usuário está ativo.'
                                                u'Desmarque esta opção ao invés de deletar a conta.'))
    bank_balance = models.DecimalField('Saldo', max_digits=10, decimal_places=2, default=0)
    date_joined = models.DateTimeField(verbose_name=_(u'Criado em'), auto_now_add=True)
    objects = EpiUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    class Meta:
        verbose_name = _(u'usuário')
        verbose_name_plural = _(u'usuários')


    def get_short_name(self):
        return self.full_name.split()[0] if self.full_name else self.email

    def get_full_name(self):
        return self.full_name