# Generated by Django 4.1.4 on 2022-12-22 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminCus', '0002_alter_demodb_options_demodb_hero_count_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demodb',
            name='hero_count',
        ),
        migrations.RemoveField(
            model_name='demodb',
            name='villian_count',
        ),
        migrations.AddField(
            model_name='demodb',
            name='hero_set',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='demodb',
            name='villain_set',
            field=models.IntegerField(default=0),
        ),
    ]