from fastapi import FastAPI
import json
app = FastAPI()


@app.get('/tabuada/{num}')
async def tabuada(num: int):
    dicionario = {}
    for i in range(1,11):
        chave = f"{num} X {i}"
        valor = num * i
        dicionario[chave]  = valor

    json_return = json.dumps(dicionario)
    return dicionario
