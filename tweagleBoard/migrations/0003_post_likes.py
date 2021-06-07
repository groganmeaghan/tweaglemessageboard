# Generated by Django 3.2.3 on 2021-06-04 19:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tweagleBoard', '0002_post_post_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='tweag_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]