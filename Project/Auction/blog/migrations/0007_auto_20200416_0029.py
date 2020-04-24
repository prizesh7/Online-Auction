# Generated by Django 2.1.7 on 2020-04-15 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200415_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='product_category',
            field=models.CharField(choices=[('electronic', 'electronic'), ('propertie', 'propertie'), ('art', 'art')], default='art', max_length=256),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('bidding', 'bidding'), ('unsold', 'unsold'), ('sold', 'sold')], default='bidding', max_length=50),
        ),
    ]