# Generated by Django 3.0.4 on 2020-03-16 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0005_auto_20200315_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='icon',
            field=models.CharField(blank=True, max_length=50, verbose_name='图标'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='name',
            field=models.CharField(max_length=30, unique=True, verbose_name='名称'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='path',
            field=models.CharField(blank=True, max_length=158, verbose_name='路径'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='pid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rbac.Menu', verbose_name='上级菜单'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='sort',
            field=models.IntegerField(blank=True, verbose_name='排序'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(max_length=60, verbose_name='组织'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='pid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rbac.Organization', verbose_name='父类组织'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='type',
            field=models.CharField(choices=[('company', '公司'), ('department', '部门')], default='company', max_length=20, verbose_name='类型'),
        ),
        migrations.AlterField(
            model_name='permission',
            name='code',
            field=models.CharField(max_length=100, unique=True, verbose_name='权限代号'),
        ),
        migrations.AlterField(
            model_name='permission',
            name='name',
            field=models.CharField(max_length=30, unique=True, verbose_name='权限'),
        ),
        migrations.AlterField(
            model_name='role',
            name='code',
            field=models.CharField(max_length=100, unique=True, verbose_name='角色代号'),
        ),
        migrations.AlterField(
            model_name='role',
            name='desc',
            field=models.CharField(blank=True, max_length=50, verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='role',
            name='name',
            field=models.CharField(max_length=32, unique=True, verbose_name='角色'),
        ),
        migrations.AlterField(
            model_name='role',
            name='permissions',
            field=models.ManyToManyField(blank=True, to='rbac.Permission', verbose_name='权限'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='加入时间'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_department', to='rbac.Organization', verbose_name='部门'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='email',
            field=models.EmailField(blank=True, max_length=50, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='mobile',
            field=models.CharField(blank=True, max_length=11, verbose_name='电话'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='password',
            field=models.CharField(max_length=100, verbose_name='密码'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='position',
            field=models.CharField(blank=True, max_length=50, verbose_name='职位'),
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='roles',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='roles',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_roles', to='rbac.Role', verbose_name='角色'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='superior',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rbac.UserInfo', verbose_name='上级主管'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='username',
            field=models.CharField(max_length=20, unique=True, verbose_name='账号'),
        ),
    ]
