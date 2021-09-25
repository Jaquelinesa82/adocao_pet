# Generated by Django 3.2.7 on 2021-09-23 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sos_animal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pet',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='pet'),
        ),
    ]
