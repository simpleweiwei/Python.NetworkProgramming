from wsgiref.simple_server import make_server
import time
from jinja2 import Template


# WSGI借助jinja2模版响应动态页面


def index():
    # 把ActivePage.html页面读进来,使用jinja2渲染后返回
    data = open('ActivePage.html', 'r+').read()
    template = Template(data)
    result = template.render(name='ww',
                             age='25',
                             time=str(time.time()),
                             user_list=['linux', 'python', 'big data'],
                             num=1)
    return [bytes(result, 'utf8')]


url_list = [
    ('/index', index)
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
