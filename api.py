from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def hello_world():
    return {"hello" : "world"}

# if __name__ == '__main__':
#     uvicorn.run(app, host="127.0.0.1", port = 8000)
# ✅ Ça permet de lancer l’API directement avec python mon_fichier.py sans utiliser la ligne de commande uvicorn mon_fichier:app --reload.
# ✅ Ça empêche uvicorn.run() de s’exécuter si le fichier est importé dans un autre script.

@app.get("/component/{component_id}")
async def get_component(component_id: int):
    return {"component_id" : component_id}

@app.get("/component/")
async def read_component(number: int, text: str):
    return {"number" : number, "text" :text}
# <url>/?number=12&text=component%20name