# Generated by Django 3.0.5 on 2020-08-31 08:52

from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=254, null=True)),
                ('author', models.CharField(blank=True, max_length=254, null=True)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
