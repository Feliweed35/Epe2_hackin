from reconbot import ReconBot

if __name__ == "__main__":
    domain = "google.com"  # Cambia por el dominio que quieres analizar
    api_url = "http://localhost:8000/api/classify/"  # Cambia por la URL de tu API REST IA
    bot = ReconBot(domain, api_url)
    bot.run()