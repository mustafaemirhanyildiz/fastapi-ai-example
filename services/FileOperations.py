from typing import List, BinaryIO
from fastapi import UploadFile
import zipfile
import rarfile
import docx2txt
from PyPDF2 import PdfReader



def ReadFiles(files: List[UploadFile]):
    rawText = ""
    for file in files:
        if (file.content_type == "application/pdf"):
            rawText += ReadPdf(file.file)
        elif (file.content_type == "text/plain"):
            rawText += ReadTxt(file.file)
        elif (file.content_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document"):
            rawText += ReadDocx(file.file)
        else:
            pass
    return rawText

def ReadPdf(fileStream: BinaryIO):
    raw_text = ""
    pdfReader = PdfReader(fileStream)
    for page in pdfReader.pages:
        if (page.extract_text() != None):
            raw_text += page.extract_text()
    return raw_text

def ReadDocx(fileStream: BinaryIO):
    doc = docx2txt.process(fileStream)
    return doc


def ReadTxt(fileStream: BinaryIO):
    return fileStream.read().decode("utf-8")