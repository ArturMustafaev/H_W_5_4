# Generated by Django 4.0.5 on 2022-06-20 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_tag_product_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='categoru',
            new_name='category',
        ),
    ]
