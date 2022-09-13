from django.contrib import admin

# Register your models here.
from self_service_portal.posts.models import Post, PostCategory


@admin.register(PostCategory)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "status",
        "category",
        "slug",
        "image",
        "image_tag",
        "published_on",
        "created_on",
        "updated_on",
    ]
    readonly_fields = ["slug", "published_on"]
    list_filter = ["status", "published_on", "created_on"]
    search_fields = ["title"]

    def image_tag(self, obj):
        from django.utils.html import mark_safe

        if obj.image:
            return mark_safe("<img width='150px' src='{}' />".format(obj.image.url))
        else:
            return ""

    image_tag.short_description = "Image"
