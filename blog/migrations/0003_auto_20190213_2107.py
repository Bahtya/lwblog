# Generated by Django 2.1.1 on 2019-02-13 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190213_2106'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='authorname',
            new_name='author',
        ),
    ]
