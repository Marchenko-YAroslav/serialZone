# Generated by Django 4.1.6 on 2023-06-15 12:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_serial_age_alter_serial_date_of_issue_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='serial',
            old_name='date_of_issue',
            new_name='dateOfIssue',
        ),
        migrations.AlterField(
            model_name='serial',
            name='description',
            field=models.TextField(max_length=260),
        ),
        migrations.AlterField(
            model_name='serial',
            name='trailer',
            field=models.FileField(upload_to='trailer', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'webm'])]),
        ),
        migrations.AlterField(
            model_name='series',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
