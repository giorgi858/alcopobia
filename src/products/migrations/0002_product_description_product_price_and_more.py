# Generated by Django 5.0 on 2023-12-27 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=True, max_digits=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.TextField(blank=True, null=True),
        ),
    ]
