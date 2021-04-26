import socket


def verify(data):
    """验证客户端握手信息"""
    data = data[:-4].split('\r\n')
    method = data.pop(0)  # 取出请求方式和协议
    header = {}
    # 将列表转为字典
    for key, val in enumerate(data):
        try:
            name, value = val.split(':')
        except Exception as exc:
            name, host, port = val.split(':')
            value = '{}:{}'.format(host, port)
        header[name] = value

    # 不满足条件则False
    if any(['GET' not in method, 'HTTP/1.1' not in method,
            header.get('Connection') != 'Upgrade',
            header.get('Upgrade') != 'websocket',
            header.get('Sec-WebSocket-Version') != '13',
            not header.get('Sec-WebSocket-Key'),
            not header.get('Origin')]):
        return False
    return True


def set_response(status):
    """设置响应头"""
    head = {'Status Code': '101 Web Socket Protocol Handshake', 'Connection': 'Upgrade', 'Upgrade': 'websocket',
            'Sec-WebSocket-Accept': 'T5ar3gbl3rZJcRmEmBT8vxKjdDo='}
    if not status:
        head = {'Status Code': '403'}
    headers = ['{}:{}'.format(k, item) for k, item in head.items()]
    headers.append('\r\n')
    res = '\r\n'.join(headers)
    return res.encode('utf8')


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # 创建TCP套接字
    s.bind(('localhost', 50007))  # 绑定地址和端口
    s.listen(1)  # 只允许同时1个客户端连接
    client_socket, client_addr = s.accept()  # 客户端对象和客户端地址
    with client_socket:
        # 读取客户端发送的消息
        data = client_socket.recv(1024).decode('utf8')
        print(data)
        status = verify(data)  # 校验握手信息
        resp = set_response(status)  # 根据握手校验结果返回响应头
        client_socket.send(resp)
        client_socket.close()
