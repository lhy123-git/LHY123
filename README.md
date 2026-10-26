# 员工管理系统 (ems)

基于 Django 4.2 的员工管理系统。

## 功能

- 部门管理：列表、新增、编辑
- 用户管理：列表、新增、编辑

## 运行

1. 配置 MySQL 数据库：修改 `ems/settings.py` 中的 `DATABASES` 配置（默认连接本机 `127.0.0.1:3306`，用户名 `root`）
2. 执行数据库迁移：

   ```bash
   python manage.py migrate
   ```

3. 启动服务：

   ```bash
   python manage.py runserver
   ```

4. 浏览器访问 http://127.0.0.1:8000
