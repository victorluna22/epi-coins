#encoding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from account.models import EpiUser
from product.models import Product
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_slack import slack_message

CREDIT = 1
DEBIT = 0

TYPES_ACTIVITIES = (
	(CREDIT, "Crédito"),
	(DEBIT, "Débito"),
	)

class Order(models.Model):
	user = models.ForeignKey(EpiUser, related_name="orders")
	value = models.DecimalField(verbose_name=_(u'Valor'), max_digits=10, decimal_places=2, default=0)
	created_at = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return "%s" % (self.user.get_short_name())

	class Meta:
		verbose_name = _(u'compra')
		verbose_name_plural = _(u'compras')


class OrderItem(models.Model):
	order = models.ForeignKey(Order, related_name="items")
	product = models.ForeignKey(Product)
	qtd = models.IntegerField(verbose_name=_(u'Quantidade'))

	def __unicode__(self):
		return "%s | %s" % (self.order.user.get_short_name(), self.product.name)

	def cost(self):
		return self.qtd * self.product.price

	class Meta:
		verbose_name = _(u'item')
		verbose_name_plural = _(u'itens')

class Activity(models.Model):
	user = models.ForeignKey(EpiUser, related_name="activities")
	type = models.IntegerField('Tipo', choices=TYPES_ACTIVITIES, default=DEBIT)
	value = models.DecimalField(verbose_name=_(u'Valor'), max_digits=10, decimal_places=2, default=0)
	created_at = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return "%s | %s" % (self.user.get_short_name(), self.value)

	class Meta:
		verbose_name = _(u'transação')
		verbose_name_plural = _(u'transações')




@receiver(post_save, sender=OrderItem)
def orderitem_save_receiver(sender, instance, created, *args, **kwargs):
	if created:
		total = instance.cost()
		instance.order.value += total
		instance.order.save()
		Activity.objects.create(user=instance.order.user, type=DEBIT, value=total)
		slack_message('slack/buy_item.slack', {
		    'obj': instance,
		})


@receiver(post_save, sender=Activity)
def activity_save_receiver(sender, instance, *args, **kwargs):
	if instance.type == DEBIT:
		instance.user.bank_balance -= instance.value
	elif instance.type == CREDIT:
		instance.user.bank_balance += instance.value
		slack_message('slack/gain_credit.slack', {
		    'obj': instance,
		})
	instance.user.save()
