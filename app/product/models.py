#encoding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Product(models.Model):
	name = models.CharField('Nome', max_length=120)
	price = models.DecimalField(verbose_name=_(u'Preço'), max_digits=10, decimal_places=2, default=0)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = _(u'produto')
		verbose_name_plural = _(u'produtos')