import os
import codecs
from src.widgets.py_todo import PyTodo
from typing import List, NoReturn

class AutoSave:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load(self) -> List[dict]:
        todos = []

        if os.path.exists(self.file_path):
            with codecs.open(self.file_path, 'r', 'utf-8') as save_file:
                content = save_file.read()

            if content == "":
                return []

            for line in content.split('\n'):
                status, todo_descrip = line.split(' ', 1)

                if status == 'o':
                    todos.append({'complete': False, 'description': todo_descrip})
                elif status == '\u2713':
                    todos.append({'complete': True, 'description': todo_descrip})

        return todos

    def save(self, todos: List[PyTodo]) -> NoReturn:
        save_content: str = "" 
        
        for idx, todo in enumerate(todos):
            if todo.isChecked():
                save_content += f'\u2713 {todo.text()}'
            else:
                save_content += f'o {todo.text()}'

            if idx < len(todos)-1:
                save_content += '\n'

        with codecs.open(self.file_path, 'w', 'utf-8') as save_file:
            save_file.write(save_content)

