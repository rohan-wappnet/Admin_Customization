# Generated by Django 4.1.4 on 2022-12-22 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminCus', '0003_remove_demodb_hero_count_remove_demodb_villian_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demodb',
            name='hero_set',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='demodb',
            name='villain_set',
            field=models.CharField(default='0', max_length=20),
        ),
    ]
