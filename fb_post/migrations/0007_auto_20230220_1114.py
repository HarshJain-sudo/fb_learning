# Generated by Django 2.2.2 on 2023-02-20 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fb_post', '0006_auto_20230217_1552'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='parent_comment_id',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='post_id',
        ),
        migrations.RemoveField(
            model_name='react',
            name='post_id',
        ),
        migrations.AddField(
            model_name='comment',
            name='parent_comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fb_post.Comment'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fb_post.Post'),
        ),
        migrations.AddField(
            model_name='react',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fb_post.Post'),
        ),
        migrations.AlterField(
            model_name='react',
            name='comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fb_post.Comment'),
        ),
    ]
