# Generated by Django 5.0.1 on 2024-01-03 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Feeds', '0003_remove_like_comment_message_like_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='user',
            new_name='liked_by',
        ),
    ]
