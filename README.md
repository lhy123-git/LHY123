# 联通用户管理系统（ems）

基于 Django 的员工/用户后台管理系统：支持部门管理与用户管理两大模块。

## 功能特性

### 部门管理

- 部门列表、新增部门、编辑部门、删除部门；
- 删除操作带前端确认提示（confirm 二次确认）。

### 用户管理

- 用户列表、新增用户、编辑用户；
- 新增/编辑统一使用 ModelForm：字段、下拉选项、校验规则由模型自动生成；
- 用户名最少 3 个字符校验；
- 表单控件通过 ModelForm `__init__` 自动统一应用 Bootstrap `form-control` 样式；
- 校验失败会保留已填内容并重新渲染表单。

### 通用能力

- 页面基于 `layout.html` 公共布局（导航、Bootstrap 样式、jQuery 脚本），通过 `{% block %}` 继承；
- 前端统一使用 Bootstrap 3.4.1 + jQuery 3.6.0（CDN 引入）；
- 提交成功后统一跳转回列表页（Post-Redirect-Get，避免刷新重复提交）。

## 技术栈

| 类别 | 说明 |
| --- | --- |
| 开发语言 | Python 3.14.7（开发环境实测，待补充：最低版本要求） |
| Web 框架 | Django 6.1.2（开发环境实测；项目脚手架由 Django 4.2.30 生成） |
| 数据库 | MySQL（连接参数见 `ems/settings.py` 的 `DATABASES`，库名 `ems`） |
| 数据库驱动 | PyMySQL 1.2.3（通过 `ems/__init__.py` 中 `pymysql.install_as_MySQLdb()` 接入） |
| 前端框架 | Bootstrap 3.4.1、jQuery 3.6.0（bootcdn CDN 引入） |
| 模板引擎 | Django Templates（`layout.html` + `{% block %}` 继承） |

## 目录结构

```
LHY123/
├── manage.py                  # 项目入口
├── 启动.bat                   # Windows 一键启动脚本
├── ems/                       # 项目配置
│   ├── __init__.py            # PyMySQL 接入（install_as_MySQLdb）
│   ├── asgi.py
│   ├── settings.py            # 全局配置（数据库、时区、模板等）
│   ├── urls.py                # 项目级路由
│   └── wsgi.py
├── app01/                     # 业务应用
│   ├── __init__.py
│   ├── admin.py               # Django admin 注册（Department）
│   ├── apps.py
│   ├── models.py              # Department / UserInfo
│   ├── tests.py
│   ├── views.py               # 视图（部门、用户管理）
│   ├── migrations/            # 数据库迁移文件
│   │   ├── __init__.py
│   │   ├── 0001_initial.py
│   │   ├── 0002_department_delete_employee.py
│   │   ├── 0003_userinfo.py
│   │   └── 0004_department_rename_name_to_title.py
│   └── templates/             # 页面模板
│       ├── layout.html        # 公共布局（导航、样式、脚本）
│       ├── dept_list.html     # 部门列表
│       ├── dept_add.html      # 新增部门
│       ├── dept_edit.html     # 编辑部门
│       ├── user_list.html     # 用户列表
│       ├── user_add.html      # 新增用户
│       └── user_edit.html     # 编辑用户
└── .gitignore                 # Git 忽略规则
```

## 快速开始

### 1. 环境依赖

- Python 3.14.x（开发环境实测，待补充：项目要求的最低 Python 版本）
- Django 6.1.2
- MySQL 数据库服务（本项目使用 MySQL 存储数据）
- PyMySQL 1.2.3（连接 MySQL 所需，替代 mysqlclient）

### 2. 获取代码并安装依赖

```bash
# 获取代码
git clone https://github.com/lhy123-git/LHY123.git
cd LHY123

# 创建并激活虚拟环境（可选，但推荐）
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

# 安装依赖
pip install Django==6.1.2 PyMySQL==1.2.3
```

### 3. 准备数据库

在 MySQL 中创建数据库（库名需与 `ems/settings.py` 中 `DATABASES` 的 `NAME` 一致，默认为 `ems`）：

```sql
CREATE DATABASE ems DEFAULT CHARACTER SET utf8mb4;
```

然后按本机环境修改 `ems/settings.py` 中的数据库连接（当前默认为本地开发配置 `root/123456@127.0.0.1:3306`，部署前请修改）：

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ems',                    # 数据库名
        'USER': 'root',                   # 数据库账号
        'PASSWORD': '123456',             # 数据库密码
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}
```

### 4. 执行数据库迁移

```bash
# 生成迁移文件（模型有改动时才需要）
python manage.py makemigrations

# 执行迁移，建表
python manage.py migrate
```

### 5. 启动服务

```bash
python manage.py runserver
```

浏览器访问 http://127.0.0.1:8000
