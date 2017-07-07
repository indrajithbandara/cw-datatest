from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


# 定义ORM
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(120), unique=True)
    done = db.Column(db.Boolean)

    def __init__(self, title, description, done):
        self.title = title
        self.description = description
        self.done = done

    def __repr__(self):
        return '<Todo %r>' % self.title
        

# 创建表格、插入数据
@app.before_first_request
def create_db():
    # Recreate database each time for demo
    #db.drop_all()
    db.create_all()

    tasks = [Todo('Buy groceries', 'Milk, Cheese, Pizza, Fruit, Tylenol', False),
             Todo('Learn Python', 'Need to find a good Python tutorial on the web', False),
             Todo('Mow the lawn', 'Find out some tools', False)]
    db.session.add_all(tasks)
    db.session.commit()


# ==================================
# 下面是RESTful api
# ==================================

@app.route('/')
def index():
    return render_template('formdata_vue.html')

        
# ==================================
# 下面是RESTful api
# ==================================

# 辅助函数
from flask import url_for
def replace_id_to_uri(task):
    return dict(uri = url_for('get_task', task_id=task.id, _external=True),
                title = task.title,
                description = task.description,
                done = task.done)


# 查询全部
@app.route('/todo/api/v1.0/tasks/', methods=['GET'])
def get_tasks():
    tasks = Todo.query.all()
    return jsonify({'tasks': list(map(replace_id_to_uri, tasks))})


# 查询一个
from flask import abort
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = Todo.query.filter_by(id=task_id).first()
    if task is None:
        abort(404)
    
    return jsonify({'task': replace_id_to_uri(task)})
    
    
# 添加
from flask import request
@app.route('/todo/api/v1.0/tasks/', methods=['POST'])
def create_task():
    # 没有数据，或者数据缺少 title 项，返回 400，表示请求无效
    if not request.json or not 'title' in request.json:
        abort(400)
    
    task = Todo(request.json['title'], request.json.get('description', ""), False)
    
    db.session.add(task)
    db.session.commit()
    return jsonify({'task': replace_id_to_uri(task)}), 201


# 更新
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Todo.query.filter_by(id=task_id).first()
    if task is None:
        abort(404)
    
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    
    task['title'] = request.json.get('title', task['title'])
    task['description'] = request.json.get('description', task['description'])
    task['done'] = request.json.get('done', task['done'])
    
    #db.session.update(task)
    db.session.commit()
    return jsonify({'task': replace_id_to_uri(task)})


# 删除
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Todo.query.filter_by(id=task_id).first()
    if task is None:
        abort(404)
    
    db.session.delete(task)
    db.session.commit()
    return jsonify({'result': True})
    
    
    
# 定制404出错页面
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404



if __name__ == '__main__':
    app.run(debug=True)