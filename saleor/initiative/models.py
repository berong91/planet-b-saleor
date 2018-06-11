from django.db import models
from django.utils import timezone
from saleor.account.models import Address


class InitiativePortfolio:
    email = models.EmailField(unique=True)
    addresses = models.ManyToManyField(Address)
    date_joined = models.DateTimeField(default=timezone.now, editable=False)
    default_contact_address = models.ForeignKey(
        Address, related_name='+', null=True, blank=True,
        on_delete=models.SET_NULL)


class Initiative(models.Model):
    slug = models.SlugField(unique=True, max_length=100)
    title = models.CharField(max_length=200)
    metadata = models.TextField(max_length=100)
    description = models.TextField()

    is_visible = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    available_on = models.DateField(blank=True, null=True)
