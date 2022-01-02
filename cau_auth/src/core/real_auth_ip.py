import os
import sys

root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(root_path)
import requests


def get_real_auth_ip():
    response = requests.get('http://10.3.38.7')
    redirected_url = response.url
    # http://10.3.191.8 => 10.3.191.8
    redirected_ip = redirected_url.split('/')[2]
    return redirected_ip


def main():
    print(get_real_auth_ip())
    pass


if __name__ == '__main__':
    main()
