from fastapi import FastAPI

app = FastAPI()

@app.get("/client/{client_id}")
def items(client_id: int):
    return {
        "n_": client_id,
        "adresse1": f"item_{client_id}",
        "adresse2": f"item_{client_id}",
        "cp": f"item_{client_id}",
        "ville": f"item_{client_id}"
    }