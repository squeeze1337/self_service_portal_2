# Generated by Django 3.2.15 on 2022-09-13 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_postimages'),
    ]

    operations = [
        migrations.AddField(
            model_name='postimages',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.post', verbose_name='Post'),
        ),
    ]
