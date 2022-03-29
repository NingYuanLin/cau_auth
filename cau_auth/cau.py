import os
import sys

root_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(root_path)
from src.helper import init_helper
from src.core import login
from src.core import logout
from src.core import check_status
from src.core import create_config


def main():
    try:
        init_args = init_helper.get_init_args()
    except ValueError as e:
        print(str(e))
        exit(1)
    else:
        action = init_args['action']
        username = init_args['username']
        password = init_args['password']
        if action == 'login':
            print('正在登录账户')
            is_success, msg = login.login(username, password)
            if is_success == 1:
                print('登录账户成功')
            else:
                print(f'登录账户失败，错误信息:{msg}')
        elif action == 'logout':
            print('正在注销账户')
            logout.force_logout()
            print('账户注销结束')
        elif action == 'check_status':
            status_info_dict = check_status.check_status()
            is_login = status_info_dict['login']
            if is_login == 1:
                login_username = status_info_dict['username']
                print(f'账号已经登录，当前登录的用户为:{login_username}')
            else:
                print('当前未登录')
        elif action == 'create_config':
            try:
                create_config.create_config()
            except FileExistsError as e:
                print(e)
                exit(1)
            else:
                print(f'配置文件生成成功')
        else:
            print('参数不合法：请指定行为（-i：登录；-o：注销；-s：检查登录状态；-c：在用户根目录下创建配置文件）')
            exit(1)

    pass


if __name__ == '__main__':
    main()
