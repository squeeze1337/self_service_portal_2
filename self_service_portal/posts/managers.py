from django.db import models
from django.utils import timezone


class PostManager(models.Manager):
    def published(self, **kwargs):
        return self.filter(published_on__lte=timezone.now())
        # return self.filter(status=self.PostStatus.PUBLISHED, **kwargs)
