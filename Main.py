from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from app.integracao.analisar_video import analisar_video_e_gerar_relatorio
import shutil
import os

app = FastAPI()

app.mount("/app/relatorio/output", StaticFiles(directory="app/relatorio/output"), name="static")

@app.post("/upload/")
async def upload_video(file: UploadFile = File(...)):
    try:
        temp_path = f"samples/{file.filename}"
        os.makedirs("samples", exist_ok=True)
        with open(temp_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        resumo, paths = analisar_video_e_gerar_relatorio(temp_path)
        pdf_link = paths["pdf"]
        md_link = paths["markdown"]

        return {
            "mensagem": "Análise concluída",
            "resumo": resumo,
            "relatorios": {
                "pdf": pdf_link,
                "markdown": md_link
            }
        }
    except Exception as e:
        return JSONResponse(content={"erro": str(e)}, status_code=500)
