FROM python:3.12

EXPOSE 8080
WORKDIR /app

COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . ./

ENTRYPOINT ["streamlit", "run", "app-gemini.py", "--server.port=8080", "--server.address=0.0.0.0", "--browser.gatherUsageStats=false"]
