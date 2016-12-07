from wsgiref.simple_server import make_server

# WSGI响应静态页面


def index():
    # 把index页面读进来返回给用户
    indexfile = open('index.html', 'r+').read()
    return [bytes(indexfile, 'utf8')]


def login():
    loginfile = open('login.html', 'r+').read()
    return [bytes(loginfile, 'utf8')]


url_list = [
    ('/index', index),
    ('/login', login)
]


def RunServer(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    # 根据url的不同,返回不同的字符串
    # 1 获取URL[URL从哪里获取?当请求过来之后执行RunServer,wsgi给咱们封装了这些请求,这些请求都封装到了,environ & start_response]
    request_url = environ['PATH_INFO']
    print(request_url)
    # 2 根据URL做不同的相应
    # print environ #这里可以通过断点来查看它都封装了什么数据
    # 循环这个列表 找到你打开的url 返回url对应的函数
    for url in url_list:
        if request_url == url[0]:
            return url[1]()
    else:
        # url_list列表里都没有返回404
        return [bytes('<h1>404 not found</h1>', 'utf8')]


if __name__ == '__main__':
    httpd = make_server('', 8000, RunServer)
    print("Serving HTTP on port 8000...")
    httpd.serve_forever()
