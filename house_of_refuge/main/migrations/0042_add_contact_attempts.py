# Generated by Django 3.2.12 on 2022-03-09 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0041_auto_20220319_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='contact_attempts',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='housingresource',
            name='status',
            field=models.CharField(choices=[('new', 'Świeżak'), ('taken', 'Zajęta'), ('calling', 'Dzwonimy'), ('ignore', 'Ignoruj')], default='new', max_length=32),
        ),
        migrations.AlterField(
            model_name='submission',
            name='status',
            field=models.CharField(choices=[('new', 'Świeżak'), ('searching', 'Szukamy'), ('in_progress', 'Host znaleziony'), ('contact_attempt', 'Próba kontaktu'), ('gone', 'Zniknęła'), ('success', 'Sukces'), ('cancelled', 'Nieaktualne')], default='new', max_length=32),
        ),
        migrations.AddField(
            model_name='submission',
            name='suspend_till',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='housingresource',
            name='contact_attempts',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='housingresource',
            name='suspend_till',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='housingresource',
            name='status',
            field=models.CharField(choices=[('new', 'Świeżak'), ('taken', 'Zajęta'), ('calling', 'Dzwonimy'),
                                            ('contact_attempt', 'Próba kontaktu'), ('ignore', 'Ignoruj')],
                                   default='new', max_length=32),
        ),
    ]
