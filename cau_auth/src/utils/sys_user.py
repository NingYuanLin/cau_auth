import getpass
import os


def get_sys_login_user():
    return getpass.getuser()


def get_sys_login_user_home_path():
    login_user_home_path = os.path.join('/home', get_sys_login_user())
    return login_user_home_path


def get_config_file_path():
    # config_file_path = os.path.join(get_sys_login_user_home_path(), '.cau_auth_config')
    config_file_path = os.path.join(os.path.expanduser('~'), '.cau_auth_config')
    return config_file_path


if __name__ == '__main__':
    print(get_sys_login_user_home_path())
