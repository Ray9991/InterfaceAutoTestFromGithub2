# Generated by Django 2.0.7 on 2018-08-28 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('case_name', models.CharField(max_length=50, null=True, verbose_name='用例名称')),
                ('req_path', models.CharField(max_length=15, null=True, verbose_name='请求路径')),
                ('req_method', models.CharField(max_length=8, null=True, verbose_name='请求方式')),
                ('req_param', models.CharField(max_length=200, null=True, verbose_name='请求参数')),
                ('resp_code', models.CharField(max_length=10, null=True, verbose_name='响应的状态码')),
                ('resp_result', models.CharField(max_length=200, null=True, verbose_name='响应结果')),
                ('test_result', models.CharField(max_length=20, null=True, verbose_name='测试结果')),
            ],
            options={
                'verbose_name': '测试用例',
                'db_table': 'testcase',
            },
        )

    ]
