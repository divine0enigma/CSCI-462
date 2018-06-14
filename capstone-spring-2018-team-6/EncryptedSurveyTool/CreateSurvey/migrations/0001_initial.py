# Generated by Django 2.0.3 on 2018-04-03 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_field', models.CharField(default='NULL', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_number', models.IntegerField()),
                ('question_field', models.CharField(max_length=500)),
                ('encrypted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interview_uuid', models.CharField(max_length=36, verbose_name='Interview unique identifier')),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('survey_title', models.CharField(max_length=500)),
                ('anonymous', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='response',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CreateSurvey.Survey'),
        ),
        migrations.AddField(
            model_name='question',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CreateSurvey.Survey'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CreateSurvey.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='response',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CreateSurvey.Response'),
        ),
        migrations.AlterUniqueTogether(
            name='answer',
            unique_together={('response', 'question')},
        ),
    ]
