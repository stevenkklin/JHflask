from flask import Flask, render_template, request, jsonify
from gevent import pywsgi
import tool

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        content = request.get_json()

        
        data = content['content']
        print('前端传来的数据:', data)
        output = tool.data_process(data)

        print('处理后的数据:', output)
        # 在这里处理数据并返回响应

        return jsonify(output)
    else:
        return "数据有问题"


if __name__ == '__main__':
	app.run(host = '0.0.0.0')
