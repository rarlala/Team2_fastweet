# Generated by Django 2.2.9 on 2020-01-17 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0004_auto_20200117_0145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='threads',
            field=models.ManyToManyField(blank=True, null=True, related_name='ThreadOrigin', to='threads.Thread'),
        ),
    ]
