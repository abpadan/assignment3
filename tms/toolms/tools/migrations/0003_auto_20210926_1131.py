# Generated by Django 2.2 on 2021-09-26 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0002_auto_20210926_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tool',
            name='name',
            field=models.CharField(default=' ', max_length=200),
        ),
    ]
