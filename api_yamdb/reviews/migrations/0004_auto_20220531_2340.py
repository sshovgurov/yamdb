# Generated by Django 2.2.16 on 2022-05-31 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20220531_2217'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='review',
            new_name='review_id',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='title',
            new_name='title_id',
        ),
    ]
