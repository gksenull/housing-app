# Generated by Django 3.2.12 on 2022-03-02 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20220301_1606'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='extra',
        ),
        migrations.AddField(
            model_name='submission',
            name='can_stay_with_pets',
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='submission',
            name='description',
            field=models.CharField(default='', help_text='Opisz grupę, podaj wiek wszystkich osób, relacje ich łączące (rodzina, przyjaciele?), zaznacz czy można ich rozbić na mniejsze', max_length=2048),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='submission',
            name='origin',
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='submission',
            name='traveling_with_pets',
            field=models.CharField(max_length=1024, null=True),
        ),
    ]