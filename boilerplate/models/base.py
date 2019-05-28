from django.db import models
from .utils import md5

class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

@receiver(post_save, sender=Example)
def create_hash(sender, instance, **kwargs):
  if not instance.hashed:
    instance.hashed = md5(str(instance.id) + str(instance.created_at))
    instance.save()
