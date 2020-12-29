# 

## 环境

- python3

## 运行

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
