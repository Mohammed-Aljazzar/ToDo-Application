# Generated by Django 5.1.5 on 2025-03-11 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0002_alter_todoitem_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='due_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
