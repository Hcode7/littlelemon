# Generated by Django 4.2 on 2023-04-17 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_menu_img_alter_menu_description_alter_menu_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='img',
            new_name='imgage',
        ),
    ]
