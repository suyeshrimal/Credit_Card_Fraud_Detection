from fastapi import FastAPI, File, Query, UploadFile,HTTPException
from fastapi.responses import FileResponse,PlainTextResponse
import uvicorn
import joblib
import numpy as np
from pydantic import BaseModel

app=FastAPI(
    title="Credit Card Fraud Detection",
    debug=True
)

model=joblib.load('best_model_decision_tree.pkl')

@app.get("/",response_class=PlainTextResponse)
async def running():
    note = """
Credit Card Fraud Detection API 🙌🏻

Note: add "/docs" to the URL to get the Swagger UI Docs or "/redoc"
  """
    return note

favicon_path='favicon.png'
@app.get('/favicon.png',include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)

class fraudDetection(BaseModel):
    step:int
    amount:float	
    oldbalanceorig:float	
    newbalanceorig:float	
    oldbalancedest:float	
    newbalancedest:float	
    isflaggedfraud:float
    cash_in:float
    cash_out:float
    debit:float
    payment:float
    transfer:float

@app.post('/predict')
def predict(data: fraudDetection):
    features = np.array([[data.step, data.amount, data.oldbalanceorig, data.newbalanceorig, data.oldbalancedest, data.newbalancedest, data.isflaggedfraud,data.cash_in,data.cash_out,data.debit,data.payment,data.transfer]])
    model = joblib.load('best_model_decision_tree.pkl')

    predictions = model.predict(features)
    if predictions == 1:
        return {"fraudulent"}
    elif predictions == 0:
        return {"not fraudulent"}
