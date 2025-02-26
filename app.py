from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

@app.get("/call-provider")
def call_provider():
    try:
        # Calling the provider container using its service name.
        response = requests.get("http://provider-service.myservices.local:8000/dynamodb", timeout=5)
        response.raise_for_status()
        return {"provider_response": response.json()}
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error calling provider: {str(e)}")
