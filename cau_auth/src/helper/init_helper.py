import os
import sys

root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(root_path)
from src.utils import args_parser
from src.utils import sys_user


def read_info_from_config():
    config_file_path = sys_user.get_config_file_path()
    if not os.path.exists(config_file_path):
        print(f'配置文件路径不存在:{config_file_path},请手动指定用户名和密码，例如：cau -i -u 用户名 -p 密码')
        return None, None
    # print(f'config_file_path:{config_file_path}')
    # config_file_path = os.path.join(root_path, 'statics/config_test.txt')
    config_file_reader = open(config_file_path, 'r', encoding='utf8')
    config_info_dict = {}
    for config_line in config_file_reader:
        config_line = config_line.strip()
        # 是不是空行
        if len(config_line) == 0:
            continue

        # 是不是以#号开头
        if config_line[0:1] == '#':
            continue

        # 找有没有等号=
        equal_symbol_index = config_line.find('=')
        if equal_symbol_index == -1:
            continue

        # 如果在一行中有等号出现
        key = config_line[0:equal_symbol_index].strip()
        value = config_line[equal_symbol_index + 1:].strip()
        config_info_dict[key] = value

    config_file_reader.close()
    username = config_info_dict.get('username')
    password = config_info_dict.get('password')

    return username, password

    pass


def get_init_args():
    """
    获取初始化参数
    系统会先尝试读取启动参数
    如果启动参数不够或不全，则会读取当前登录用户根目录下的配置文件，例如/home/ning/.cau_auth_config
    :return:
    """
    args = args_parser.get_parse_res()

    if args.logout:
        action = 'logout'
    elif args.check_status:
        action = 'check_status'
    elif args.create_config:
        action = 'create_config'
    elif args.login:
        action = 'login'
    else:
        action = 'none'

    username = args.username
    password = args.password

    # 当当前的行为是login，并且用户名和密码有一个未被指定时
    if action == 'login' and (
            (username is None and password is not None) or (username is not None and password is None)):
        raise ValueError('username和password必须同时指定或者都不指定(这时会读取用户根目录下的.cau_auth_config文件)')

    # 当当前的行为是login，并且用户名和密码未被全部指定时，
    if action == 'login' and username is None and password is None:
        # 读取配置文件
        username, password = read_info_from_config()
        # 判断是否顺利读取到了username和password
        if username is None or password is None:
            raise ValueError('读取配置文件出错')

    init_args = {
        'action': action,
        'username': username,
        'password': password
    }

    return init_args


def test_read_info_from_config():
    print(read_info_from_config())


if __name__ == '__main__':
    test_read_info_from_config()
