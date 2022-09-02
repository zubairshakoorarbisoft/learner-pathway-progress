# Generated by Django 3.2.15 on 2022-09-01 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learner_pathway_progress', '0002_historicallearnerpathwayprogress_learnerpathwayprogress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicallearnerpathwayprogress',
            name='learner_pathway_uuid',
            field=models.UUIDField(editable=False, verbose_name='LEARNER_PATHWAY_UUID'),
        ),
        migrations.AlterField(
            model_name='learnerpathwayprogress',
            name='learner_pathway_uuid',
            field=models.UUIDField(editable=False, verbose_name='LEARNER_PATHWAY_UUID'),
        ),
    ]
