from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.management.utils import get_random_secret_key


class KeysUser(AbstractUser):
    pass

class InternalKey(models.Model):
    """
    Internal-only API keys.
    """
    name = models.CharField(max_length=200)
    material = models.CharField(max_length=200, default=get_random_secret_key)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='internal_keys',
    )
    created = models.DateTimeField(auto_now_add=True)
    last_used = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    active = models.BooleanField(default=True)
  
    def __str__(self):
        return f"{self.name} ({self.owner})"
    

    class Meta:
        indexes = [
            models.Index(fields=['material']),
        ]


class ExternalKey(models.Model):
    """
    Real API keys - sensitive!
    """
    name = models.CharField(max_length=200)
    material = models.CharField(max_length=200)
    domain = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    last_used = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='external_keys',
        null=True,
        blank=True,
    )
    active = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.name} ({self.domain})"


class AuditRecord(models.Model):
    """
    Use names rather than foreign keys to avoid
    referential integrity issues.
    """
    class Action(models.TextChoices):
        CREATE = 'CREATE'
        READ = 'READ'
        UPDATE = 'UPDATE'
        DELETE = 'DELETE'

    user_name = models.CharField(max_length=200)
    internal_key_name = models.CharField(max_length=200)
    external_key_name = models.CharField(max_length=200)
    action = models.CharField(
        max_length=10,
        choices=Action.choices
    )
    timestamp = models.DateTimeField()
    
    def __str__(self):
        return (
            f"{self.user} {self.action}"
            f"{self.external_key_name} using "
            f"{self.internal_key_name} at {self.timestamp}"
        )
