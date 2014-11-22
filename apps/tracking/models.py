from model_utils.models import TimeStampedModel
from django.db import models
from utils.base_62_converter import dehydrate


class Link(TimeStampedModel):
    url = models.URLField()
    slug = models.CharField(max_length=32, db_index=True)

    @property
    def count_redirects(self):
        return self.logs.count()

    def __str__(self):
        return self.url

    def __unicode__(self):
        return self.url

    def save(self, **kwargs):
        is_new = not self.pk
        super(Link, self).save(**kwargs)
        if is_new:
            self.slug = dehydrate(self.pk)
            super(Link, self).save(update_fields=['slug'])


class LogItem(TimeStampedModel):
    link = models.ForeignKey(Link, related_name='logs')
    ip_address = models.GenericIPAddressField()
    referrer = models.CharField(max_length=255, blank=False, null=False)
