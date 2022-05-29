# Provides code to connect the CLI with the to-do database

"""This module provides the RP To-Do model-controller."""
# todo/todo_.py

from typing import Any, Dict, NamedTuple
from pathlib import Path
from todo.database import DatabaseHandler
from typing import Any, Dict, List, NamedTuple
from todo import DB_READ_ERROR

class Todoer:
    def __init__(self, db_path: Path) -> None:
        self._db_handler = DatabaseHandler(db_path)
    def add(self,description: List[str], priority: int = 2 ):
        
        """Add a new to-do to the database."""
        description_text = " ".join(description)
        if not description_text.endswith("."):
            description_text += "."
        todo = {
            "Description": description_text,
            "Priority": priority,
            "Done": False,
        }
        read = self._db_handler.read_todos()
        if read.error == DB_READ_ERROR:
            return CurrentTodo(todo, read.error)
        read.todo_list.append(todo)
        write = self._db_handler.write_todos(read.todo_list)
        return CurrentTodo(todo, write.error)
    


class CurrentTodo(NamedTuple):
    todo: Dict[str, Any]
    error: int