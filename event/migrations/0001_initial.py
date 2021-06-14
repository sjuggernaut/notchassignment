# Generated by Django 3.2.4 on 2021-06-13 15:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('createdAt', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=45)),
                ('environment', models.CharField(max_length=15)),
                ('component', models.CharField(max_length=15)),
                ('message', models.TextField()),
                ('data', models.TextField()),
            ],
        ),
    ]
