from . import *

class Example(Base):
  name = models.CharField(max_length=100, null=True)
  hashed = models.CharField(max_length=32, blank=True, null=True)

  class Meta:
    db_table = 'example'
    verbose_name_plural = 'examples'

  def __str__(self):
    if self.name:
        return name
    return 'default'

@receiver(post_save, sender=Example)
def create_hash(sender, instance, **kwargs):
  if not instance.hashed:
    instance.hashed = md5(str(instance.id) + str(instance.created_at))
    instance.save()
