from typing import Union
from fastapi import FastAPI, UploadFile
import uvicorn
from services.FileOperations import ReadFiles
from services.ChatWithPdf import chatWithGpt
from services.ChatWithPdf import chatWithGoogleAi

app = FastAPI()


@app.post("/chatWithGpt")
def read_root(file: UploadFile, userInput: str):
    input = ReadFiles([file])
    response = chatWithGpt(pdfText=input, userInput=userInput)
    return response


@app.post("/chatWithGoogleAi")
def read_root(file: UploadFile, userInput: str):
    input = ReadFiles([file])
    response = chatWithGoogleAi(pdfText=input, userInput=userInput)
    return {"response": response}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=5231)