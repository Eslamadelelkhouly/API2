# Generated by Django 5.0 on 2023-12-10 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=300)),
                ('image', models.CharField(default='', max_length=700)),
                ('price', models.IntegerField()),
                ('author_name', models.CharField(default='', max_length=250)),
                ('rating', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, default='', max_length=20)),
                ('password', models.CharField(default='', max_length=20)),
            ],
        ),
    ]
