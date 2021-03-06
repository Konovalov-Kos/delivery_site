# Generated by Django 3.0.5 on 2020-05-16 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_category_order_product_store'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.Product')),
            ],
        ),
    ]
