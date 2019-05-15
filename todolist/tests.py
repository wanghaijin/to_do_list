from django.test import TestCase
from .models import Task
# Create your tests here.

t = Task(task_name = '阅读', is_do = False)
t.save()

Task.objects.creat(task_name = '阅读', is_do = False)

#首先尝试获取，不存在就创建，可以防止重复
Task.objects.get_or_create(task_name = '阅读', is_do = False)


#查询所有is_do = False的对象
Task.objects.filter(is_do=False)

#查询所有对象
Task.objects.all()

Task.objects.count()

#删除task_name = '睡觉'的一个对象
t = Task.objects.get(task_name = '睡觉')
t.delete()