# Generated by Django 4.1.4 on 2022-12-22 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminCus', '0004_alter_demodb_hero_set_alter_demodb_villain_set'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demodb',
            name='hero_set',
        ),
        migrations.RemoveField(
            model_name='demodb',
            name='villain_set',
        ),
    ]