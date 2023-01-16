from fastapi import FastAPI

app = FastAPI()

def go_in_the_fridge_message(true_or_false):
    return {'go_in_the_fridge': true_or_false}


@app.get("/go-in-the-fridge/{food}")
async def go_in_the_fridge(food: str):
    if food == 'cheese':
        return go_in_the_fridge_message(True)
    else:
        return go_in_the_fridge_message(False)
