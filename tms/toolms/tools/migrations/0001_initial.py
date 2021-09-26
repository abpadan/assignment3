# Generated by Django 2.2 on 2021-09-26 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('available', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=' ', max_length=50)),
                ('manufacturer', models.CharField(default=' ', max_length=50)),
                ('available', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='available.Available')),
            ],
        ),
    ]