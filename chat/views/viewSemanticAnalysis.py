from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class SemanticAnalysisView(APIView):
    """
    API que recibe texto y devuelve una clasificación semántica simple.
    Aquí puedes integrar tu IA real, por ahora es un ejemplo simulado.
    """

    def post(self, request):
        texto = request.data.get("text", "")
        if not texto:
            return Response({"error": "Falta el texto a analizar."}, status=status.HTTP_400_BAD_REQUEST)

        # Simulación simple de clasificación basada en keywords
        texto_lower = texto.lower()
        if any(palabra in texto_lower for palabra in ["password", "confidencial", "secreto", "privado", "clave"]):
            clasificacion = "potencialmente sensible"
        elif any(palabra in texto_lower for palabra in ["backup", "admin", "index of", "login"]):
            clasificacion = "posible interés"
        else:
            clasificacion = "irrelevante"

        resumen = f"El texto analizado fue clasificado como: {clasificacion}"

        return Response({
            "clasificacion": clasificacion,
            "resumen": resumen
        })