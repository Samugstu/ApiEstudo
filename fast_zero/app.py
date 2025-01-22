from fastapi import FastAPI

app = FastAPI()


@app.get('/tabuada/{num}')
async def tabuada(num: int):
    result = []

    for i in range(10):
        resultadoConta = f'{num} X {i} = {num * 1}'
        result.append(resultadoConta)
    return result
