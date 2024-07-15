from django.db import models


# Create your models here.
# 用户
class User(models.Model):
    name = models.CharField(max_length=10, verbose_name="姓名")
    user_id = models.CharField(max_length=7, verbose_name="员工ID")
    gender_choice = (
        (1, "男"),
        (2, "女"),
    )
    gender = models.IntegerField(choices=gender_choice, verbose_name="性别", default=1)
    birthday = models.DateField(verbose_name="出生日期", blank=True, null=True)
    department = models.ForeignKey("Department", on_delete=models.CASCADE, verbose_name="部门")
    phone_number = models.CharField(max_length=11, verbose_name="电话号码", null=True, blank=True)
    email = models.EmailField(verbose_name="邮箱", null=True, blank=True)
    user_status_choice = (
        (1, "在职"),
        (2, "离职"),
    )
    user_status = models.IntegerField(choices=user_status_choice, verbose_name="用户状态", default=1)
    position = models.CharField(max_length=10, verbose_name="职位")
    user_name = models.CharField(max_length=30, verbose_name="用户账号")
    password = models.CharField(max_length=20, verbose_name="用户密码")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间", blank=True, null=True)
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间", blank=True, null=True)
    
    class Meta:
        db_table = 'sys_user_'


# 部门


class Department(models.Model):
    depart_id = models.CharField(max_length=10, verbose_name="部门ID")
    name = models.CharField(max_length=10, verbose_name="部门名称")
    depart_status_choice = (
        (1, "启用"),
        (2, "禁用")
    )
    depart_status = models.IntegerField(choices=depart_status_choice, verbose_name="部门状态", default=1)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间", blank=True, null=True)
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间", blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    
    class Meta:
        db_table = 'sys_department_'


# 员工状态


# 请假
class Personal_leave(models.Model):
    type_choice = (
        (1, "病假"),
        (2, "事假"),
    )
    type = models.IntegerField(choices=type_choice, verbose_name="请假类型")
    name = models.CharField(max_length=10, verbose_name="姓名")
    user_id = models.CharField(max_length=7, verbose_name="员工ID")
    start_time = models.DateField(verbose_name="开始时间")
    end_time = models.DateField(verbose_name="结束时间")
    reason = models.CharField(max_length=100, verbose_name="请假原因")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间", blank=True, null=True)
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间", blank=True, null=True)
    check_status_choice = (
        (1, "待审核"),
        (2, "审核通过"),
        (3, "审核不通过"),
    )
    check_status = models.IntegerField(choices=check_status_choice, verbose_name="审核状态", default=1)
    class Meta:
        db_table = 'sys_Personal_leave_'
