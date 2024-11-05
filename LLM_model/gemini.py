from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv


load_dotenv()
    

def get():
    llm = ChatGoogleGenerativeAI(model="gemini-pro")
    return llm
     
