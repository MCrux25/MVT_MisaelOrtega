# Generated by Django 3.2.15 on 2022-10-19 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familia', '0005_avatar'),
    ]

    operations = [
        migrations.DeleteModel(
            name='familiar',
        ),
        migrations.AddField(
            model_name='suenios',
            name='titulo',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='suenios',
            name='suenio',
            field=models.CharField(max_length=1500),
        ),
    ]
