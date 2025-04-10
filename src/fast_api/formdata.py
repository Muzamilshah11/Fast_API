from fastapi import FastAPI, File, UploadFile, bytes

app = FastAPI() # Create Instance

@app.post("/form/data/filedata")
async def formdata_upload(  file1 : UploadFile, file2: bytes=File(), name:str = File() ):
    return {"Upload File": file1, "File_Bytes": len(file2),"File_Name": name}
    