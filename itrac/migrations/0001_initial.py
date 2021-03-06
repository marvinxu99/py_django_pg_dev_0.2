# Generated by Django 3.0.4 on 2020-05-19 03:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_author', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('is_resolved', models.BooleanField(default=False)),
                ('resolved_date', models.DateTimeField(blank=True, null=True)),
                ('upvotes', models.IntegerField(default=0)),
                ('tag', models.CharField(blank=True, max_length=30, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='img')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('issue_type', models.CharField(choices=[('BUG', 'bug'), ('FEATURE', 'feature')], default='BUG', max_length=9)),
                ('status', models.CharField(choices=[('TODO', 'todo'), ('DOING', 'doing'), ('DONE', 'done')], default='TODO', max_length=7)),
                ('assignee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='issue_assignee', to=settings.AUTH_USER_MODEL)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issue_author', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SavedIssue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issue_savedissue', to='itrac.Issue')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_savedissue', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reply_author', to=settings.AUTH_USER_MODEL)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reply_comment', to='itrac.Comment')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='issue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_issue', to='itrac.Issue'),
        ),
    ]
