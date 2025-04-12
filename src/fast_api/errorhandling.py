from fastapi import FastAPI, HTTPException

app = FastAPI()
Items = {1,2,3,4,5,6}
@app.get("/items/{handle_error}")
async def error_handle(item_id: int):
    if not item_id in Items:
        raise HTTPException(status_code=404, detail="Item not found. Please try again!")
    return {"item_id": item_id}
   