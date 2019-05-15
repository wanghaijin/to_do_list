from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task
# Create your views here.
# lists = [
#     {'待办事项':'睡觉','是否完成':False},
#     {'待办事项':'阅读','是否完成':True},
# ]
def home(request):
    # content = str(request.POST)
    # global lists
    # lists = Task.objects.all()
    if request.method == 'POST':
        if request.POST['待办事项'] == '':
            lists = Task.objects.all()
            content = {'清单':lists,'警告':'请输入内容'}
            return render(request,'todolist/home.html',content)
        else: 
            t = Task(task_name=request.POST['待办事项'])
            # lists.append({'待办事项': request.POST['待办事项'],'是否完成':False}) 
            t.save() 
            # content = {'待办事项': request.POST['待办事项']}
            lists = Task.objects.all()
            content = {'清单':lists,'成功':'添加成功'}
            return render(request,'todolist/home.html',content)
    else:
        lists = Task.objects.all()
        content = {'清单':lists}
        return render(request,'todolist/home.html',content)


def about(request):
    return render(request,'todolist/about.html')

def edit(request,forloop_counter):
# def edit(request):
    # global lists
    # forloop_counter = int(request.POST['存储顺序'])
    lists = Task.objects.all()
    content = {'任务':lists[int(forloop_counter)-1],'任务顺序':int(forloop_counter)-1}
    return render(request,'todolist/edit.html',content)

def line(request,forloop_counter):
    # global lists
    lists = Task.objects.all()
    t = lists[int(forloop_counter)-1]
    if t.is_do == True:
        t.is_do=False
        t.save()
    else:
        t.is_do = True
        t.save()
    return redirect("todolist:主页")

def delete(request,forloop_counter):
    # global lists
    lists = Task.objects.all()
    t = lists[int(forloop_counter)-1]
    t.delete()
    # lists.pop(int(forloop_counter)-1)
    return redirect("todolist:主页")

def changedit(request):
    # global lists
    lists = Task.objects.all()
    t = lists[int(request.POST['存储顺序'])]
    t.task_name=request.POST["内容"]
    t.save()
    # print(request.POST["内容"])
    # print(lists)
    return redirect("todolist:主页")
