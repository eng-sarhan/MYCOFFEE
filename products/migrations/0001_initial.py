# Generated by Django 4.1 on 2023-08-23 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('photo', models.ImageField(upload_to='photos/%y/%m/%d/')),
                ('is_active', models.BooleanField(default=True)),
                ('publish_date', models.DateTimeField()),
            ],
            options={
                'ordering': ['-publish_date'],
            },
        ),
    ]
