from fastapi import FastAPI
import logging
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import json
from typing import List, Dict
from fastapi.middleware.cors import CORSMiddleware

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"]
)

class ToDoItem(BaseModel):
    id: int
    title: str
    isEditItem: bool

# Percorso al file JSON che contiene i dati
JSON_FILE_PATH = "items.json"

# Funzione per caricare i dati dal file JSON
def load_data() -> List[Dict]:
    try:
        with open(JSON_FILE_PATH, "r") as file:
            return json.load(file)
        
    except FileNotFoundError:
        print("FileNotFoundError")
        return []  # Se il file non esiste, ritorna una lista vuota
    except json.JSONDecodeError:        
        print("FileNotFoundError")
        return []  # Se il file è vuoto o malformato, ritorna una lista vuota

# Endpoint GET per ottenere i dati
@app.get("/tasks", response_model=List[Dict])
def get_tasks():
    tasks = load_data()  # Carica i dati dal file JSON
    return JSONResponse(content=tasks['items'])

@app.post("/tasks", response_model=List[ToDoItem])
def add_taks(task: ToDoItem):
    data = load_data()
    #logger.debug(task)
    data["items"].append(task.model_dump())

    with open(JSON_FILE_PATH, 'w') as f:
        json.dump(data, f)

    return data