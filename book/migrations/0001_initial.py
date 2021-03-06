# Generated by Django 2.1.7 on 2019-03-14 10:20

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='unique id for each book', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('Create', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('family', models.CharField(max_length=300)),
                ('Email', models.EmailField(blank=True, max_length=254)),
                ('born', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Writer'),
        ),
    ]
