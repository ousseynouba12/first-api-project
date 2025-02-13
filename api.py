from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


# Le schéma que va définir comment les données recue  doivent être
class CoordIn(BaseModel):
    password : str 
    # dans les infos reçue on doit avoir le mdp
    # mais on ne va pas le renvoyer (voir class CoordOut)
    lat : float
    lon : float
    zoom : Optional[int] = None

# Le schéma que va définir comment les données recue  doivent être
class CoordOut(BaseModel):
    password : str 
    lat : float
    lon : float
    zoom : Optional[int] = None

@app.get("/")
async def hello_world():
    return {"hello" : "world"}

# méthodee post sans paramètre avec filtrage de donnée envoyé
@app.post("/position/", response_model=CoordOut, response_model_exclude={'password'})
async def make_position(coord: CoordIn):
    return coord

# @app.post("/position/", response_model=CoordOut)
# async def make_position(coord: CoordIn):
#     return coord
#Pour cette méthode ne pas meettre password dans CoordOut

# methode post avec paramètre
@app.post("/position/{priority}")
async def make_position(priority: int, coord: CoordIn, value: bool):
    return{"priority": priority, "new_coord": coord.dict(), "value": value}













# if __name__ == '__main__':
#     uvicorn.run(app, host="127.0.0.1", port = 8000)
# ✅ Ça permet de lancer l’API directement avec python mon_fichier.py sans utiliser la ligne de commande uvicorn mon_fichier:app --reload.
# ✅ Ça empêche uvicorn.run() de s’exécuter si le fichier est importé dans un autre script.

# @app.get("/component/{component_id}")
# async def get_component(component_id: int):
#     return {"component_id" : component_id}

# @app.get("/component/")
# async def read_component(number: int, text: str):
#     return {"number" : number, "text" :text}
# # <url>/?number=12&text=component%20name