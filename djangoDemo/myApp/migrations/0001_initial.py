# Generated by Django 2.2.1 on 2019-07-06 03:06

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gname', models.CharField(max_length=20)),
                ('gdate', models.DateField()),
                ('ggirlnum', models.IntegerField()),
                ('gboynum', models.IntegerField()),
                ('isDelete', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=20)),
                ('sgender', models.BooleanField(default=True)),
                ('sage', models.IntegerField()),
                ('scontend', models.CharField(max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
                ('lastTime', models.DateTimeField(auto_now=True)),
                ('createTime', models.DateTimeField(auto_now_add=True)),
                ('sgrade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.Grades')),
            ],
            options={
                'db_table': 't_student',
                'ordering': ['id'],
            },
            managers=[
                ('stuObj0', django.db.models.manager.Manager()),
            ],
        ),
    ]
