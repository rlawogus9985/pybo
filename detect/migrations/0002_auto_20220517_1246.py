# Generated by Django 3.1.3 on 2022-05-17 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detect', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='uploadFile',
        ),
        migrations.AddField(
            model_name='document',
            name='uploadedFile',
            field=models.FileField(null=True, upload_to='Uploaded Files/'),
        ),
        migrations.AlterField(
            model_name='document',
            name='dateTimeOfUpload',
            field=models.DateTimeField(),
        ),
    ]
