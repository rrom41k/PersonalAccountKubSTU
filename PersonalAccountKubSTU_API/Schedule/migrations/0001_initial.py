# Generated by Django 4.2.7 on 2023-11-21 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('content', models.TextField(blank=True)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('content', models.TextField(blank=True)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=1)),
                ('time_start', models.CharField(max_length=5)),
                ('time_end', models.CharField(max_length=5)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('content', models.TextField(blank=True)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Schedule.department')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('specialization', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Schedule.specialization')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('patronymic', models.CharField(max_length=255, null=True)),
                ('pas_data', models.CharField(max_length=255)),
                ('telephone', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Schedule.group')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='specialization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Schedule.specialization'),
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time_of_exam', models.DateTimeField()),
                ('grading', models.CharField(max_length=1)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Schedule.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Schedule.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('patronymic', models.CharField(max_length=255, null=True)),
                ('pas_data', models.CharField(max_length=255)),
                ('telephone', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Schedule.department')),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='institute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Schedule.institute'),
        ),
        migrations.CreateModel(
            name='Classes_Sheldue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroom', models.CharField(max_length=10)),
                ('day_of_the_week', models.CharField(max_length=30)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Schedule.employee')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Schedule.group')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Schedule.lesson')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Schedule.subject')),
            ],
        ),
    ]