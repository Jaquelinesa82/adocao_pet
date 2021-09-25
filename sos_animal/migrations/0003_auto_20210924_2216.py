# Generated by Django 3.2.7 on 2021-09-25 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sos_animal', '0002_auto_20210923_1254'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='photo',
            new_name='file',
        ),
        migrations.AlterField(
            model_name='pet',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='pet',
            name='phone',
            field=models.CharField(max_length=11, null=True),
        ),
    ]