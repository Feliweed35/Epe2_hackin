from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import dns.resolver

class DomainRequest(BaseModel):
    domain: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def resolve_dns(domain):
    record_types = ['A', 'MX', 'NS', 'SOA', 'TXT']
    dns_records = {}
    resolver = dns.resolver.Resolver()
    resolver.nameservers = ['8.8.8.8', '8.8.4.4']
    resolver.lifetime = 5

    for record_type in record_types:
        try:
            answers = resolver.resolve(domain, record_type)
            dns_records[record_type] = [rdata.to_text() for rdata in answers]
        except Exception as e:
            dns_records[record_type] = [f"Error: {str(e)}"]
    return dns_records

def generar_resumen_ia(texto: str) -> str:
    resumen = []

    if "admin" in texto:
        resumen.append("Se menciona acceso administrativo.")
    if "backup" in texto:
        resumen.append("Se hace referencia a una copia de seguridad.")
    if ".env" in texto or "config" in texto:
        resumen.append("Posible archivo de configuración expuesto.")
    if "claro.com" in texto or "aliexpress.com" in texto:
        resumen.append("Se detectaron dominios potencialmente sensibles.")

    if not resumen:
        return "No se encontraron elementos críticos en el texto."

    return " ".join(resumen)

@app.post("/api/analyze/")
def analyze_domain(payload: DomainRequest):
    domain = payload.domain.lower()
    texto = f"Analizando el dominio: {domain}"

    riesgo = "riesgo bajo"
    razones = []

    if "admin" in domain or "backup" in domain:
        riesgo = "riesgo medio"
        razones.append("Palabras clave como 'admin' o 'backup' detectadas.")

    if "env" in domain or "xml" in domain:
        riesgo = "riesgo alto"
        razones.append("Posibles archivos de configuración expuestos: 'env', 'xml'.")

    if "claro.com" in domain or "aliexpress.com" in domain:
        riesgo = "riesgo alto"
        razones.append("Se encontraron dominios potencialmente sensibles como 'claro.com' o 'aliexpress.com'.")

    if not razones:
        razones.append("No se detectaron patrones sensibles.")

    dns_resultados = {
        domain: resolve_dns(domain)
    }

    resumen_ia = generar_resumen_ia(texto)

    return {
        "clasificacion": riesgo,
        "resumen": " ".join(razones),
        "dns": dns_resultados,
        "resumen_ia": resumen_ia
    }
