import os
import sys
from turtle import title

from django.db import models
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

    class BlogStatus(models.TextChoices):
        DRAFT = "DRAFT", _("Entwurf")
        PUBLISHED = "PUBLISHED", _("Veröffentlicht")

    status = models.CharField(
        _("Status"), max_length=50, choices=BlogStatus.choices, default=BlogStatus.DRAFT
    )
    title = models.CharField(_("Titel"), max_length=250)
    sub_title = models.CharField(_("Untertitel"), max_length=250, blank=True, null=True)
    image = models.ImageField(
        _("Cover Image"),
        upload_to="blog/cover_images/",
        height_field=None,
        width_field=None,
        max_length=None,
    )
    conten = models.TextField(_("Blog Inhalt"), blank=True, null=True)
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
