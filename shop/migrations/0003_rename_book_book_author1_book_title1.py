# Generated by Django 5.0.1 on 2024-01-29 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_rename_author1_book_book_remove_book_title1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='book',
            new_name='author1',
        ),
        migrations.AddField(
            model_name='book',
            name='title1',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
