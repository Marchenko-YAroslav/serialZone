# Generated by Django 4.1.6 on 2023-06-15 12:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_serial_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serial',
            name='age',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='serial',
            name='date_of_issue',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='serial',
            name='raiting',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='serial',
            name='trailer',
            field=models.FileField(upload_to='trailer', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'avi'])]),
        ),
        migrations.AlterField(
            model_name='series',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
