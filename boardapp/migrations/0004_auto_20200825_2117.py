# Generated by Django 2.2.15 on 2020-08-25 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0003_auto_20200825_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardmodel',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]