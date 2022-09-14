# Generated by Django 3.2.15 on 2022-09-14 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_postimages_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Titel')),
                ('comment', models.TextField(verbose_name='Kommentar')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Kommentar',
                'verbose_name_plural': 'Kommentare',
                'ordering': ['-created_on'],
            },
        ),
    ]
