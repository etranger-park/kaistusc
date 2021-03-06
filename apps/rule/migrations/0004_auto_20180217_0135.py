# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-02-17 01:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rule', '0003_auto_20180216_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='chapter_type',
            field=models.CharField(choices=[('SEC', '절'), ('SUPPL', '부칙'), ('PRE', '전문'), ('CHAP', '장')], max_length=8, verbose_name='종류'),
        ),
        migrations.AlterField(
            model_name='rule',
            name='revision_type',
            field=models.CharField(choices=[('ESTAB', '제정'), ('PART', '일부개정'), ('FULL', '전부개정')], max_length=8, verbose_name='제개정 종류'),
        ),
        migrations.AlterField(
            model_name='rule',
            name='rule_type',
            field=models.CharField(choices=[('BYLAW', '세칙'), ('ETC', '기타규정'), ('CONST', '회칙'), ('RULE', '규칙')], max_length=8, verbose_name='종류'),
        ),
    ]
