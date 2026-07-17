"""
generar_pdf.py — Convierte INFORME.md a INFORME.pdf.

1. Renderiza el Markdown a HTML (con estilos y soporte de tablas/código).
2. Usa LibreOffice en modo headless para convertir el HTML a PDF.

Requisitos:
    pip install markdown
    LibreOffice instalado (comando `soffice` o `libreoffice`).

Uso:
    python generar_pdf.py
"""

import shutil
import subprocess
import sys
from pathlib import Path

import markdown

MD_FILE = Path("INFORME.md")
HTML_FILE = Path("INFORME.html")

CSS = """
<style>
  body { font-family: 'Liberation Sans', Arial, sans-serif; font-size: 11pt;
         line-height: 1.45; color: #1a1a1a; margin: 2.5cm; }
  h1 { font-size: 20pt; border-bottom: 2px solid #333; padding-bottom: 6px; }
  h2 { font-size: 15pt; margin-top: 22px; color: #16324f; }
  h3 { font-size: 12pt; color: #16324f; }
  code { background: #f2f2f2; padding: 1px 4px; border-radius: 3px;
         font-family: 'Liberation Mono', monospace; font-size: 9.5pt; }
  pre { background: #f6f8fa; border: 1px solid #ddd; border-radius: 5px;
        padding: 10px; overflow-x: auto; font-size: 9pt; }
  pre code { background: none; padding: 0; }
  table { border-collapse: collapse; width: 100%; margin: 10px 0; }
  th, td { border: 1px solid #bbb; padding: 6px 9px; text-align: left;
           font-size: 10pt; vertical-align: top; }
  th { background: #16324f; color: #fff; }
  tr:nth-child(even) td { background: #f4f7fa; }
  blockquote { border-left: 4px solid #16324f; margin: 10px 0; padding: 4px 14px;
               color: #444; background: #f8f9fb; }
</style>
"""


def main():
    if not MD_FILE.exists():
        sys.exit(f"No se encontró {MD_FILE}")

    texto = MD_FILE.read_text(encoding="utf-8")
    cuerpo = markdown.markdown(
        texto, extensions=["tables", "fenced_code", "toc", "sane_lists"]
    )
    html = f"<!DOCTYPE html><html lang='es'><head><meta charset='utf-8'>{CSS}</head><body>{cuerpo}</body></html>"
    HTML_FILE.write_text(html, encoding="utf-8")
    print(f"HTML generado: {HTML_FILE}")

    soffice = shutil.which("soffice") or shutil.which("libreoffice")
    if not soffice:
        sys.exit("LibreOffice no encontrado. Instala 'libreoffice' o convierte el HTML manualmente.")

    print("Convirtiendo a PDF con LibreOffice...")
    subprocess.run(
        [soffice, "--headless", "--convert-to", "pdf", "--outdir", ".", str(HTML_FILE)],
        check=True,
    )
    print("Listo: INFORME.pdf")


if __name__ == "__main__":
    main()
