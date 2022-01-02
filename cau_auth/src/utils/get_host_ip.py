import socket


def get_host_ip():
    """
    查询本机ip地址
    :return:
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip


def main():
    print(get_host_ip())


if __name__ == '__main__':
    main()
