# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from lib.batch_clone_from_gitlab import get_all_projects_from_gitlab, batch_clone_from_gitlab
from lib.batch_push_to_github import batch_push_to_github

gitlab_addr = 'ip:port'
gitlab_token = 'ymsSzk' # 见gitlab官网或你的gitlab私服
github_token = '5737a6' # 见你的github
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    batch_clone_from_gitlab(gitlab_addr, gitlab_token)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
