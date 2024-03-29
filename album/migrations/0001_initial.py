# Generated by Django 4.2.2 on 2023-06-23 03:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('image_id', models.AutoField(primary_key=True, serialize=False)),
                ('image_url', models.CharField(max_length=255)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'image',
                'ordering': ['-upload_date'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('tag_id', models.AutoField(primary_key=True, serialize=False)),
                ('tag_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'tag',
                'ordering': ['tag_name'],
            },
        ),
        migrations.CreateModel(
            name='ImageTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='album.image')),
                ('tag_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='album.tag')),
            ],
            options={
                'db_table': 'image_tag',
                'ordering': ['image_id', 'tag_id'],
            },
        ),
    ]
