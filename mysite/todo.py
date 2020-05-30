import json
from Todo.mysite import my


class Todo:
    todo = dict()
    id = 0

    def load_todo(self):
        with open('D:/1.json', 'r') as f:
            todo_str = f.read()
            if len(todo_str) == 0:
                self.todo = dict()
                self.id = 0
            else:
                self.todo = json.loads(todo_str)
                self.id = int(list(my.get_dict_last(self.todo).keys())[0])
                print('最后一个元素ID：', self.id)

    def save_todo(self):
        with open('D:/1.json', 'w') as f:
            f.write(json.dumps(self.todo))

    def add_msg(self, todoing):
        self.id = self.id + 1
        self.todo[self.id] = {
            'todo': todoing,
            'ac': False,
            'com': False,
        }

    def remove_msg(self, id):
        del self.todo[id]

    def activate(self):
        for k, v in self.todo.items():
            if v['ac']:
                print(k, '==', v)

    def add_completed(self, id):
        for k, v in self.todo.items():
            if int(k) == id:
                self.todo[k]['com'] = True
                self.todo[k]['ac'] = False
            else:
                self.todo[k]['ac'] = True

    def completed(self):
        for k, v in self.todo.items():
            if v['com']:
                print(k, '==', v)


if __name__ == '__main__':
    Todo = Todo()
    Todo.load_todo()
    # Todo.add_msg(input('要做的事：'))
    # Todo.remove_msg(input('删除id：'))

    Todo.add_completed(5)
    # Todo.completed()

    Todo.activate()
    # print(Todo.todo)
    Todo.save_todo()
