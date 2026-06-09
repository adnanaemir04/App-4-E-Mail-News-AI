from langchain.chat_models import init_chat_model
GOOGLE_API_KEY = "AQ.Ab8RN6IPAIRkR1ZqnxEOauu98wn898MCf_f-iWV9BwooTqmleQ"

model = init_chat_model(
    model="gemini-3-flash-preview",
    model_provider="google-genai",
    api_key=GOOGLE_API_KEY
)

response = model.invoke("Kurşun Kalem mi Daha iyi Tükenmez Kalem Mi?")
response_str = response.content[0]['text']
print(response_str)