import os
import sys

root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(root_path)

import argparse


def get_parse_res():
    with open(os.path.join(root_path, 'statics/argparse_description.txt')) as reader:
        parser = argparse.ArgumentParser(description=reader.read())

    parser.add_argument('-i', '--login', action="store_true", help='登录校园网')
    parser.add_argument('-o', '--logout', action="store_true", help='注销校园网')
    parser.add_argument('-s', '--check_status', action="store_true", help='检查登录状态')
    parser.add_argument('-c', '--create_config', action="store_true", help='在用户根目录下创建配置文件')

    parser.add_argument('-u', '--username', help="cau校园网的用户名", type=str)
    parser.add_argument('-p', '--password', help='cau校园网的密码', type=str)

    args = parser.parse_args()

    return args


def test():
    print(get_parse_res())
    pass


if __name__ == '__main__':
    test()
