import os
import sys
from turtle import title

from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext as _


# Create your models here.
class Post(models.Model):
    """Post model needs the following fields:
    * status (DRAFT, PUBLISHED)
    * author --> Foreign Key User
    * title
    * sub_title
    * content
    * slug
    * image
    * published_on
    * created_on
    * updated_on
    """

    class PostStatus(models.TextChoices):
        DRAFT = "DRAFT", _("Entwurf")
        PUBLISHED = "PUBLISHED", _("Veröffentlicht")

    status = models.CharField(
        _("Status"), max_length=50, choices=PostStatus.choices, default=PostStatus.DRAFT
    )
    title = models.CharField(_("Titel"), max_length=250)
    sub_title = models.CharField(_("Untertitel"), max_length=250, blank=True, null=True)
    image = models.ImageField(
        _("Cover Image"),
        upload_to="Post/cover_images/",
        height_field=None,
        width_field=None,
        max_length=None,
    )
    conten = models.TextField(_("Post Inhalt"), blank=True, null=True)
    slug = models.SlugField(
        _("Slug"), blank=True, null=True, help_text=_("Titel als Url")
    )
    published_on = models.DateTimeField(
        _("Veröffentlicht am"),
        auto_now=False,
        auto_now_add=False,
        blank=True,
        null=True,
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        ordering = ["-created_on"]
        get_latest_by = ["-created_on"]

    def __str__(self):
        # return str(self.pk) + "-" + self.title
        return "{} - {}".format(self.pk, self.title)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
