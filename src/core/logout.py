import json
import os
import sys
import time

root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(root_path)
import requests
from src.core import real_auth_ip
from src.core import check_status
from src.utils import get_host_ip


def logout():
    """
    :return: dr1002({"result":1,"wopt":0,"msg":14,"uid":"","hidm":0,"hidn":-5,"ss5":"10.2.246.167","ss6":"10.3.38.7","vid":0,"ss1":"000d48448ce8","ss4":"000000000000","cvid":0,"pvid":0,"hotel":0,"aolno":20122,"eport":-1,"eclass":1,"time":7372,"flow":4936051,"fsele":1,"fee":0,"v6af":0,"v6df":0,"actM":1,"actt":129,"actdf":56,"actuf":0,"act6df":0,"act6uf":0,"allfm":2,"d1":224,"u1":138,"d2":0,"u2":0,"o1":0,"nd1":224,"nu1":138,"nd2":0,"nu2":0,"no1":0})
    """
    auth_ip = real_auth_ip.get_real_auth_ip()
    url = f"http://{auth_ip}/drcom/logout?callback=dr1002&v=7912"

    headers = {
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
        'Accept': '*/*',
        'Referer': 'http://10.3.38.7/',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': 'PHPSESSID=mve8c7kvtso03dqcknjsu22bv1'
    }

    response = requests.request("GET", url, headers=headers)

    return response.text.strip()

    pass


def get_live_device_list(ac):
    """
    :param ac: 用户名
    :return: [{"sessionid":36976,"logintime":"2021-10-09 10:16:00","loginip":"10.6.53.8","loginmac":"3C22FB958456","devicetype":"PC"}]
    """
    # 获取毫秒时间戳
    msec_timestamp = int(time.time() * 1000)

    # 获取在线设备
    url = f"""
        http://10.3.38.7:801/eportal/?c=ServiceInterface&a=loadOnlineDevice&callback=jQuery111307422641681895024_{msec_timestamp}&account={ac}&_={msec_timestamp}
        """
    response = requests.get(url)
    response_text = response.text
    # jQuery111309758939784360352_1633746542401({"result ... }) => {"result ... }
    response_dict = response_text[response_text.find('{'):-1]
    response_dict = json.loads(response_dict)
    data = response_dict['data']
    return data


def _force_logout(ac, session_id):
    # 获取毫秒时间戳
    msec_timestamp = int(time.time() * 1000)

    url = f"""
    http://10.3.38.7:801/eportal/?c=ServiceInterface&a=offlineUserDevice&callback=jQuery111308603583689084444_{msec_timestamp}&account={ac}&sessionid={session_id}&_=1633747340884
    """
    response = requests.get(url)
    response_text = response.text
    response_dict = response_text[response_text.find('{'):-1]
    response_dict = json.loads(response_dict)
    result = response_dict['result']
    if result == 'ok':
        return True
    else:
        return False

    pass


def get_local_session_id(ac):
    # 获取在线设备列表
    live_device_list = get_live_device_list(ac)

    # 获取当前机器的ip
    host_ip = get_host_ip.get_host_ip()

    # 匹配当前机器的session_id
    for live_device in live_device_list:
        login_ip = live_device['loginip']
        if login_ip == host_ip:
            session_id = live_device['sessionid']
            return session_id

    # 啥也没找到
    return None


def force_logout():
    # 先检查是否登录，如果没有登录，就不用执行了
    status_info_dict = check_status.check_status()
    if status_info_dict['login'] == 0:
        print('当前未登录，不需要登出')
        return False

    # 如果登录了，就获取登录名
    ac = status_info_dict['AC']

    # 获取当前设备的session_id
    session_id = get_local_session_id(ac)
    if session_id is None:
        print('ERROR:未在登录设备中找到本机')

    # 登出
    _force_logout(ac, session_id)
    print('登出成功')
    return True

    pass


def main():
    # print(logout())
    force_logout()


if __name__ == '__main__':
    main()
