import requests
from send_email import send_email
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os

load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")
news_api_key = os.getenv("NEWS_API_KEY")

url = (
    "https://newsapi.org/v2/top-headlines?"
    "category=business&"
    "language=en&"
    "pageSize=8&"
    "sortBy=publishedAt&"
    "apiKey=" + news_api_key
)

response = requests.get(url)
content = response.json()

articles = content.get("articles", [])

news_text = "\n".join(
    f"{a.get('title', '')} - {a.get('description', '')}"
    for a in articles
)

model = init_chat_model(
    model="gemini-3-flash-preview",
    model_provider="google-genai",
    api_key=google_api_key
)

prompt = f"""
Sen bir finans haber analistisin.
Aşağıdaki haberleri analiz et.
Eğer kısaltması "FCEL,SATL,NEXR" olan 3 şirketten,
herhangi biriyle alakalı bir haber yayınlanırsa onu analiz et ve mutlaka haber ver.
ÖZELLİKLE SATL'a dikkat et.
Analizini şu şekilde paylaş:
1-Genel Borsa Analizi (1 paragraf)
2-SIKI TAKİP ETTİĞİNİZ ŞİRKETLER HAKKINDA HABERLER(yukarda bahsedilen 3 şirket) (detaylı analiz):
3-SATL teknik ve takip analizi.
4- Bu 3 Hissenin Günlük fiyat Hareketlerinin trader mantığıyla yorumu.
şeklinde benimle paylaş.Ve her şirketin haberinin yanına şirketin kısaltmasını ekle.
Haberler:
{news_text}
"""

result = model.invoke(prompt)

# 🔥 SADECE TEXT ÇIKAR (signature vs. yok)
response_text = result.content

# Eğer yine structured gelirse fallback:
if isinstance(response_text, list):
    response_text = response_text[0].get("text", "")

body = "Subject: News Summary\n\n" + response_text

send_email(body.encode("utf-8"))
