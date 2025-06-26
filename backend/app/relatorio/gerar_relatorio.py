from fpdf import FPDF
import os

def gerar_relatorio_pdf(texto: str, caminho: str) -> str:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    for linha in texto.split("\n"):
        pdf.multi_cell(0, 10, linha)
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    pdf.output(caminho)
    return caminho

def gerar_relatorio_md(texto: str, caminho: str) -> str:
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    with open(caminho, "w") as f:
        f.write(texto)
    return caminho
