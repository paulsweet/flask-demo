from flask import Flask,url_for,render_template

app = Flask(__name__)

name = 'momo'
movies = [{'title': 'My Neighbor Totoro', 'year': '1988'},
          {'title': 'Dead Poets Society', 'year': '1989'},
          {'title': 'A Perfect World', 'year': '1993'},
          {'title': 'Leon', 'year': '1994'},
          {'title': 'Mahjong', 'year': '1996'},
          {'title': 'Swallowtail Butterfly', 'year': '1996'},
          {'title': 'King of Comedy', 'year': '1999'},
          {'title': 'Devils on the Doorstep', 'year': '1999'},
          {'title': 'WALL-E', 'year': '2008'},
          {'title': 'The Pork of Music', 'year': '2012'}]

@app.route('/')
def index():

    return render_template("index.html",name=name,movies=movies) # 变量通过render_template返回

# @app.route('/usr/<name>')
# def usr_page(name):
#     return 'usr: %s' % name
#
# @app.route('/test')
# def test_url_for():     # 下面是一些调用示例：
#     print(url_for('hello_world'))  # 输出：/     # 注意下面两个调用是如何生成包含 URL 变量的 URL 的
#     print(url_for('usr_page', name='greyli'))  # 输出：/user/greyli
#     print(url_for('usr_page', name='peter'))  # 输出：/user/peter
#     print(url_for('test_url_for'))  # 输出：/test
#     print(url_for('test_url_for', num=2))
#     return 'Test page'

if __name__ == '__main__':
    app.run()