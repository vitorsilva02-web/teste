from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI(
    title="AutoMind AI",
    description="Assistente experimental para análise de sintomas automotivos.",
    version="0.1.0",
)

app.mount("/static", StaticFiles(directory="static"), name="static")


class DiagnosticRequest(BaseModel):
    vehicle: str
    symptoms: str
    codes: str = ""


@app.get("/", response_class=HTMLResponse)
def home():
    with open("static/index.html", "r", encoding="utf-8") as file:
        return file.read()


@app.get("/health")
def health():
    return {"status": "online", "project": "AutoMind AI", "version": "0.1.0"}


@app.post("/diagnostico")
def diagnose(request: DiagnosticRequest):
    # Primeira versão: estrutura de entrada e triagem simples.
    # A análise por IA será conectada em uma próxima etapa.
    symptoms = request.symptoms.strip()
    codes = request.codes.strip()

    if not symptoms and not codes:
        return {
            "status": "incomplete",
            "message": "Informe os sintomas ou pelo menos um código de falha.",
        }

    possibilities = []
    text = f"{symptoms} {codes}".lower()

    if "superaque" in text or "temperatura" in text:
        possibilities.append(
            "Verificar nível e circulação do líquido de arrefecimento, "
            "ventoinha, válvula termostática e sensor de temperatura."
        )
    if "bateria" in text or "alternador" in text or "voltagem" in text:
        possibilities.append(
            "Verificar tensão da bateria em repouso e durante a partida, "
            "sistema de carga, aterramentos e conexões."
        )
    if "falha" in text or "engasg" in text or "p030" in text:
        possibilities.append(
            "Investigar ignição, alimentação de combustível, entrada falsa de ar "
            "e compressão; não substituir peças sem realizar testes."
        )

    if not possibilities:
        possibilities.append(
            "Registrar os dados do veículo, reproduzir o sintoma e realizar "
            "medições antes de definir uma causa."
        )

    return {
        "status": "preliminary",
        "vehicle": request.vehicle,
        "message": "Triagem inicial gerada. As hipóteses precisam ser confirmadas por testes.",
        "possible_checks": possibilities,
        "important": (
            "Esta versão não lê módulos do veículo e não substitui "
            "diagnóstico presencial ou procedimentos do fabricante."
        ),
    }
