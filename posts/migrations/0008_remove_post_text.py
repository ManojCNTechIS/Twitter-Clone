# Generated by Django 4.1.3 on 2022-12-03 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_post_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='text',
        ),
    ]