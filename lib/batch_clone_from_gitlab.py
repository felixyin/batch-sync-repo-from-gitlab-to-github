#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-
# 在Python3.0测试通过
# 需要在gitlab里面新建一个AccessToken填入gitlabToken

import sys

if sys.version_info < (3, 0):
    import urllib
else:
    from urllib.request import urlopen

import json
import subprocess, shlex
import time
import os


#     gitlabAddr = '192.168.3.10:30000'
#     gitlabToken = 'ymsSzkQmX3Y_14KyyBJ6'
# 会自动创建gitlab文件夹用于存放所有项目
def batch_clone_from_gitlab(gitlabAddr, gitlabToken):
    for index in range(10):
        url = "http://%s/api/v4/projects?private_token=%s&per_page=100&page=%d&order_by=name" % (
            gitlabAddr, gitlabToken, index)
        print(url)

        if sys.version_info < (3, 0):
            allProjects = urllib.urlopen(url)
        else:
            allProjects = urlopen(url)

        allProjectsDict = json.loads(allProjects.read().decode(encoding='UTF-8'))
        if len(allProjectsDict) == 0:
            break
        for thisProject in allProjectsDict:
            try:
                thisProjectURL = thisProject['http_url_to_repo']
                thisProjectPath = thisProject['path_with_namespace']
                print(thisProjectURL + ' ' + thisProjectPath)

                if os.path.exists(thisProjectPath):
                    command = shlex.split('git -C "%s" pull' % (thisProjectPath))
                else:
                    command = shlex.split('git clone %s %s' % (thisProjectURL, thisProjectPath))

                resultCode = subprocess.Popen(command)
                print(resultCode)

                time.sleep(3)
            except Exception as e:
                print("--------------------> Error on %s: %s" % (thisProjectURL, e.strerror))


#
# [{'name': 'repo1',
#   'path': 'username/repo1',
#   'des': ' https://gitee.com/username/repo1'},
#   {'name': 'repo2',
#   'path': 'username/repo2',
#   'des': ' https://gitee.com/username/repo2'}]
def get_all_projects_from_gitlab(gitlab_addr, gitlab_token):
    projects = []
    for index in range(10):
        url = "http://%s/api/v4/projects?private_token=%s&per_page=100&page=%d&order_by=name" % (
            gitlab_addr, gitlab_token, index)
        print(url)

        if sys.version_info < (3, 0):
            allProjects = urllib.urlopen(url)
        else:
            allProjects = urlopen(url)

        allProjectsDict = json.loads(allProjects.read().decode(encoding='UTF-8'))
        if len(allProjectsDict) == 0:
            break
        for thisProject in allProjectsDict:
            thisProjectURL = thisProject['http_url_to_repo']
            thisProjectPath = thisProject['path_with_namespace']
            # print(thisProjectURL + ' ' + thisProjectPath)
            projects.append({
                'name': thisProjectPath.split('/', 1)[1],
                'path': thisProjectPath,
                'des': thisProjectURL
            })
    return projects
