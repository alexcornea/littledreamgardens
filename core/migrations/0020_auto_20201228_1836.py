# Generated by Django 3.0.4 on 2020-12-28 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20201228_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diy',
            name='name',
            field=models.CharField(blank=True, default=' ', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='gardens',
            name='name',
            field=models.CharField(blank=True, default=' ', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='gettingstarted',
            name='name',
            field=models.CharField(blank=True, default=' ', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='terrariums',
            name='name',
            field=models.CharField(blank=True, default=' ', max_length=100),
        ),
    ]
