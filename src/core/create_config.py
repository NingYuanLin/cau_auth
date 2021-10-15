import os
import sys

root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(root_path)
from src.utils import sys_user


def create_config():
    config_file_path = sys_user.get_config_file_path()
    if os.path.exists(config_file_path):
        raise FileExistsError('配置文件已经存在')

    # 复制配置文件
    with open(os.path.join(root_path, 'statics/config_example.txt'), 'r') as reader:
        config_example = reader.read()
        username = input('请输入你的用户名：')
        password = input('请输入你的密码：')
        config_example = config_example.replace('这里填你的用户名', username)
        config_example = config_example.replace('这里填你的密码', password)
        with open(config_file_path, 'w') as writer:
            writer.write(config_example)
