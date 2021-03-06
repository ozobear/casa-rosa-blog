# Generated by Django 2.0.1 on 2018-02-13 06:17

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20180130_0349'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artist',
            options={'ordering': ['-name']},
        ),
        migrations.AddField(
            model_name='artist',
            name='video',
            field=embed_video.fields.EmbedVideoField(blank=True),
        ),
    ]
