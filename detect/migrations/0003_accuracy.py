# Generated by Django 3.1.3 on 2022-05-21 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('detect', '0002_auto_20220517_1246'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accuracy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acc', models.CharField(max_length=100)),
                ('picture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detect.document')),
            ],
        ),
    ]