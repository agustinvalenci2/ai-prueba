# 🚀 Proyecto de Chat con LangChain y OpenAI

Este proyecto es una API basada en **FastAPI** que utiliza **LangChain** y **OpenAI** para responder preguntas y recuperar información sobre el clima mediante la API de OpenWeatherMap.

## 📌 **Características**
- Integración con modelos de lenguaje de OpenAI.
- Uso de **LangChain** para mejorar la gestión de respuestas.
- Consulta de clima en tiempo real usando **OpenWeatherMap**.
- Soporte para manejo de historial de conversación.

## 🛠 **Instalación**

1. Clona el repositorio:
   ```bash
   git https://github.com/agustinvalenci2/ai-prueba.git
   cd ai-prueba
   ```

2. Crea un entorno virtual (opcional pero recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 **Uso**

### 1️⃣ **Ejecutar la API**
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### 2️⃣ **Ejemplo de Petición (Usando cURL o Postman)**
```bash
curl -X POST "http://localhost:8000/api/chat" -H "Content-Type: application/json" -d '{"messages": [{"role": "user", "content": "¿Cuál es el clima actual en Cali, Colombia?"}]}'
```

**Respuesta esperada:**
```json
{
    "reply": "En Cali,CO, el clima actual es de nubes dispersas, con una temperatura de 27.0°C y una humedad del 57%."
}
```

## 🔑 **Configuración de API Keys**
Crea un archivo `.env` y agrega lo siguiente:
```env
OPENWEATHERMAP_API_KEY=tu_clave_api
OPENAI_API_KEY=tu_clave_api
```

## 📜 **Estructura del Proyecto**
```
📂 tu_proyecto
│-- 📂 app
│   │-- 📂 utils
│   │   ├── langchain_agent.py  # Lógica de LangChain y OpenAI
│   │-- main.py  # Punto de entrada de la API
│-- requirements.txt
│-- README.md
```

## 📌 **Dependencias Principales**
- `fastapi` (Framework para construir la API).
- `uvicorn` (Servidor ASGI para FastAPI).
- `openai` (Cliente para OpenAI API).
- `langchain` (Orquestador de modelos de lenguaje).
- `transformers` (Modelos de lenguaje como Falcon-7B).

## 🛠 **Contribuciones**
¡Sientete libre de contribuir! Crea un **pull request** o reporta problemas en la sección de **issues**.

## 📄 **Licencia**
Este proyecto está bajo la **MIT License**.


