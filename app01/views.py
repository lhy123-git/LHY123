from django.shortcuts import render, redirect
from django import forms
from . import models


# 部门列表
def dept_list(request):
    depts = models.Department.objects.all()
    return render(request, "dept_list.html", {"depts": depts})


# 新增部门
def dept_add(request):
    if request.method == "POST":
        t = request.POST.get("title")
        models.Department.objects.create(title=t)
        return redirect("/dept/")
    return render(request, "dept_add.html")


# 删除部门
def dept_del(request, did):
    models.Department.objects.filter(id=did).delete()
    return redirect("/dept/")


# 编辑部门
def dept_edit(request, did):
    obj = models.Department.objects.get(id=did)
    if request.method == "POST":
        obj.title = request.POST.get("title")
        obj.save()
        return redirect("/dept/")
    return render(request, "dept_edit.html", {"d": obj})


# ============ 用户管理（ModelForm 版本） ============
class UserModelForm(forms.ModelForm):
    # 显式字段：name 最少 3 个字符
    name = forms.CharField(min_length=3, label="用户名")

    class Meta:
        model = models.UserInfo
        fields = ["name", "password", "age", "account", "create_time", "gender", "depart"]
        # widgets 写在 __init__ 里统一加，这里不用写

    # 根据底层类源码重写 __init__：循环给所有字段自动加 form-control 样式
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 循环找到所有的插件，添加 class="form-control"
        for name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"


# 用户列表
def user_list(request):
    users = models.UserInfo.objects.all()
    return render(request, "user_list.html", {"users": users})


# 添加用户（ModelForm 版本）
def user_add(request):
    """ 添加用户（ModelForm 版本） """
    if request.method == "GET":
        form = UserModelForm()
        return render(request, "user_add.html", {"form": form})

    # 用户 POST 提交数据，数据校验：拿到 request.POST 的所有数据逐个字段校验
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        # 如果数据合法，保存到数据库（代替之前的 models.UserInfo.objects.create(..)）
        # print(form.cleaned_data)
        form.save()
        return redirect("/user/list/")

    # 校验失败：在页面上显示错误信息，并且保留原来填过的数据
    return render(request, "user_add.html", {"form": form})


# 编辑用户（ModelForm 版本）
def user_edit(request, nid):
    """ 编辑用户：根据ID获取对象，ModelForm 自动用 instance 填充默认值 """
    row_object = models.UserInfo.objects.filter(id=nid).first()
    if not row_object:
        return redirect("/user/list/")

    if request.method == "GET":
        form = UserModelForm(instance=row_object)
        return render(request, "user_edit.html", {"form": form})

    # POST：带 instance 就是 update，不带就是 create
    form = UserModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect("/user/list/")
    return render(request, "user_edit.html", {"form": form})
