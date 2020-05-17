def request_parse(ip_port, request_data):
    # 根据客户端浏览器请求的资源，返回请求资源
    request_text = request_data.decode()
    loc = request_text.find("\r\n")
    request_line = request_text[:loc]
    request_line_list = request_line.split(" ")
    # 得到相应的资源路径
    file_path = request_line_list[1]
    print("{}正在请求资源".format(ip_port))
    # 设置默认的首页
    if file_path == "/":
        file_path = "index.html"

    return file_path


def application(request_data, ip_port):

    # 响应行
    response_line = "HTTP/1.1 200 OK\r\n"
    # 响应头
    response_header = "Server:PythonWS/2.1\r\n"
    response_header += "Content-Type: text/html\r\n"
    # 响应空行
    response_blank = "\r\n"

    file_path = request_parse(ip_port, request_data)
    print(file_path)
    # 响应主体
    try:
        with open("static/"+file_path, "rb") as file:
            # 将内容返回给客户端
            response_body = file.read()

    except Exception as e:
        # 响应失败
        response_line = "HTTP/1.1 404 Not Found\r\n"
        response_body = "Error!(%s)" % str(e).encode()

    response_data = (response_line + response_header + response_blank).encode() + response_body
    # 发送响应的报文
    return response_data

