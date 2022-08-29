# Generated by Django 4.1 on 2022-08-24 11:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_delete_exceldocument_delete_filemode'),
    ]

    operations = [
        migrations.CreateModel(
            name='OsInfoFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input', models.FileField(upload_to='osinfo/input')),
                ('output', models.FileField(upload_to='osinfo/output')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]