# Generated by Django 4.0 on 2021-12-18 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hms', '0003_remove_data_sex'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='email',
        ),
        migrations.AlterField(
            model_name='data',
            name='age',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='data',
            name='bgroup',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='data',
            name='dsis',
            field=models.TextField(),
        ),
    ]
