from wsgiref.simple_server import make_server

"""

WSGI，全称 Web Server Gateway Interface，或者 Python Web Server Gateway Interface ，
是为 Python 语言定义的 Web 服务器和 Web 应用程序或框架之间的一种简单而通用的接口

很多框架都自带了 WSGI server ，比如 Flask，webpy，Django、CherryPy等等。
当然性能都不好，自带的 web server 更多的是测试用途，发布时则使用生产环境的 WSGI server或者是联合 nginx 做 uwsgi

python标准库提供的独立WSGI服务器称为wsgiref

"""


def index():
    return [bytes('<h1>index</h1>', 'utf8')]


def login():
    return [bytes('<h1>login</h1>', 'utf8')]


def reg():
    return [bytes('<h1>reg</h1>', 'utf8')]


def layout():
    return [bytes('<h1>layout</h1>', 'utf8')]


url_list = [
    ('/index', index),
    ('/login', login),
    ('/reg', reg),
    ('/layout', layout)
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
