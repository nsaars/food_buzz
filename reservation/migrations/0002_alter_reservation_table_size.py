# Generated by Django 4.0.5 on 2022-06-21 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='table_size',
            field=models.CharField(choices=[('Table Size', 'Table Size'), ('2F - 3F', '2F - 3F'), ('2.5F - 3.5F', '2.5F - 3.5F'), ('3F - 4F', '3F - 4F'), ('3.5F - 4.5F', '3.5F - 4.5F'), ('5F - 6F', '5F - 6F'), ('5.5F - 6.5', '5.5F - 6.5F')], default='Table Size', max_length=31, null=True),
        ),
    ]
