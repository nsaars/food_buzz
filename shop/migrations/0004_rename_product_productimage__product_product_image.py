# Generated by Django 4.0.5 on 2022-06-19 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_remove_product_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productimage',
            old_name='product',
            new_name='_product',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='shop.productimage'),
            preserve_default=False,
        ),
    ]