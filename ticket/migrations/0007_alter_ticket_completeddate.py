# Generated by Django 4.1.1 on 2022-10-01 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0006_alter_ticket_completeddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='completedDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
