# Generated by Django 3.2.12 on 2022-02-27 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20220227_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='housingresource',
            name='people_to_accommodate_raw',
            field=models.CharField(default='', max_length=1024),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='housingresource',
            name='accommodation_length',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='housingresource',
            name='city_and_zip_code',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='housingresource',
            name='costs',
            field=models.CharField(max_length=1024),
        ),
    ]
