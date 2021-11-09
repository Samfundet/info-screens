# Generated by Django 3.2.8 on 2021-11-09 18:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('infoscreen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_edited', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Sist redigert')),
                ('created', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Opprettet')),
                ('name', models.CharField(blank=True, max_length=140, null=True)),
                ('youtube_code', models.CharField(max_length=140)),
                ('creator', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='creator_video_set', to=settings.AUTH_USER_MODEL, verbose_name='Opprettet av')),
                ('last_editor', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='editor_video_set', to=settings.AUTH_USER_MODEL, verbose_name='Sist redigert av')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='screen',
            name='videos',
            field=models.ManyToManyField(blank=True, to='infoscreen.Video'),
        ),
    ]
