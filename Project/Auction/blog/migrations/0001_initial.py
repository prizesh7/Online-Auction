# Generated by Django 2.1.7 on 2020-04-01 19:38

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('product_category', models.CharField(choices=[('paint', 'paint'), ('art', 'art')], default='', max_length=256)),
                ('base_price', models.IntegerField(default='')),
                ('raising_price', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('sell_price', models.IntegerField(blank=True, default=0, null=True)),
                ('status', models.CharField(choices=[('bidding', 'bidding'), ('unsold', 'unsold'), ('sold', 'sold')], default='', max_length=50)),
                ('sell_customer_name', models.CharField(blank=True, default='', max_length=50)),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('hour', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(23)])),
                ('minite', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(59)])),
                ('second', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(59)])),
                ('image', models.ImageField(default='default.jpg', upload_to='product_pics')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]