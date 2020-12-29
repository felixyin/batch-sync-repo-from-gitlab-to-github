# 

gitlab github 仓库同步工具

> 仓库太多，一个一个在github配置gitlab的仓库地址太麻烦，不如写一个工具批量下载所有gitlab仓库，批量再从本地上传到github上去。

## 环境

- python3

## 运行

```
virtualenv venv
source venv/bin/activate
pip list
pip install PyGithub
pip list
```

1. 打开*.py 配置github、gitlab参数
2. clone gitlab 所有仓库到本地：
```
python3 sync-gitlab-to-local.py
```
3. 调整目录结构

` cd . `

打开batch_push_to_github.py第39行注释
或移动项目目录平铺到根目录下

> 调整项目为私有请修改private=False，为True

4.push 本地所有仓库到github 
```
python3 sync-local-to-github.py
```
