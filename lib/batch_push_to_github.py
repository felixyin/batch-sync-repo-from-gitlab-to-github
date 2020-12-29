from github import Github
import re
import os


def batch_push_to_github(github_token, projects):
    g = Github(github_token)  # token
    user = g.get_user()
    repoddl = [repo for repo in user.get_repos()]
    reponames = [repo.name for repo in repoddl]  # 当前已有的项目列表
    for i, v in enumerate(projects):
        print(v)

        project_name = v["name"]
        if project_name in reponames:  # 如果重名
            # 如果想从gitlab覆盖github仓库，请尝试打开下面注释
            # try:
            #     remote_repo = user.get_repo(project_name)  # 创建，并设置权限为私有
            #
            #     ssh_url = remote_repo.ssh_url
            #     # FIXME gitlab group下的项目，需要你自己手工移动到根目录 否则pushd无法找到从gitlab clone到本地的项目
            #     # 或者替换下面{project_name} 为 v["path"]
            #     cmd = f" pushd {project_name} && git remote rm origin && git remote add origin {ssh_url} && git push origin master && popd "
            #     print(cmd)
            #     os.system(f"bash -xc '{cmd}' 1>>  log.txt 2>>log.txt")
            #     print(f"{remote_repo} done")
            #     print("created")
            # except Exception as e:
            #     print("--------------------> 此仓库 %s 提交代码失败" % project_name)
            print("--------------------> 此仓库 %s 已存在" % project_name)
        else:
            des = re.sub("[\n\t\b]", "", v["des"])
            try:
                remote_repo = user.create_repo(project_name, description=des, private=False)  # 创建，并设置权限为私有
                # FIXME gitlab group下的项目，需要你自己手工移动到根目录 否则pushd无法找到从gitlab clone到本地的项目
                # project_name = v["path"]
                ssh_url = remote_repo.ssh_url
                cmd = f" pushd {project_name} && git remote rm origin && git remote add origin {ssh_url} && git push origin master && popd "
                print(cmd)
                os.system(f"bash -xc '{cmd}' 1>>  log.txt 2>>log.txt")
                print(f"{remote_repo} done")
                print("created")
            except Exception as e:
                print("--------------------> 此仓库 %s 创建仓库失败+提交代码失败" % project_name)

    # 上传中会出现一些项目未能成功push。 用下面的方法补漏。
    # for i,repo in enumerate(projects):
    #     cmd=f" pushd {repo['name']} && git push gh master && popd "
    #     print(cmd)
    #     os.system(f"bash -xc '{cmd}' 1>>  log.txt 2>>log.txt")
    #     print(f"{repo} done")
