# Generated by Django 2.1.4 on 2019-06-12 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_events', '0002_alter_event_field_meta'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eventindex',
            options={'verbose_name': 'Event index page', 'verbose_name_plural': 'Event index pages'},
        ),
    ]