from app.transcricao.transcribe import extrair_audio, transcrever_audio
from app.visao.analyze_video import analisar_frames
from app.relatorio.gerar_relatorio import gerar_relatorio_pdf, gerar_relatorio_md
import openai
import os

def analisar_video_e_gerar_relatorio(video_path: str):
    audio_path = extrair_audio(video_path)
    texto_transcrito = transcrever_audio(audio_path)
    elementos_visuais = analisar_frames(video_path)

    openai.api_key = os.getenv("OPENAI_API_KEY")

    prompt = f"""
Você é um especialista em acessibilidade digital. Com base no texto transcrito abaixo e nos elementos visuais detectados, avalie se o vídeo é acessível para pessoas com deficiência visual e auditiva. Indique sugestões de melhoria:

TRANSCRIÇÃO:
{texto_transcrito}

ELEMENTOS VISUAIS DETECTADOS:
{elementos_visuais}
"""

    resposta = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Você é um especialista em acessibilidade digital."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    texto_resposta = resposta["choices"][0]["message"]["content"]
    pdf_path = "app/relatorio/output/relatorio.pdf"
    md_path = "app/relatorio/output/relatorio.md"

    gerar_relatorio_pdf(texto_resposta, pdf_path)
    gerar_relatorio_md(texto_resposta, md_path)

    return texto_resposta, {
        "pdf": pdf_path,
        "markdown": md_path
    }
