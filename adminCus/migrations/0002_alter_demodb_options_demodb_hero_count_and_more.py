# Generated by Django 4.1.4 on 2022-12-22 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminCus', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='demodb',
            options={'verbose_name_plural': 'demodb'},
        ),
        migrations.AddField(
            model_name='demodb',
            name='hero_count',
            field=models.IntegerField(default=0, max_length=20),
        ),
        migrations.AddField(
            model_name='demodb',
            name='villian_count',
            field=models.IntegerField(default=0, max_length=20),
        ),
    ]
