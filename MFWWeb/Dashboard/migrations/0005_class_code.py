# Generated by Django 2.0.3 on 2018-04-17 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0004_auto_20180416_0651'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='code',
            field=models.CharField(default='Z0ksjZ', max_length=6),
        ),
    ]