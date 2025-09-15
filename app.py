
import os
from dotenv import load_dotenv
import streamlit as st
import time 

#from langchain.chat_models import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import HumanMessage  # <--- import HumanMessage

load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

#Langsmith se track krne ke liye
os.environ["LANGCHAIN_TRACING_V2"]=os.getenv("LANGCHAIN_TRACING_V2")
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

#PROMPT DESIGN
prompt=ChatPromptTemplate.from_messages([("system", "You are a helpful assistant. Respond the queries with all the important events occured on that day globally. If the date exceeds the year 2024, kindly ask the user to enter dates with year 2024 or before. If no such big historical event occured, kindly give list of events occured on another date which is closest to the user's intended date.Dont reply to other queries other than the ones containing dates."), ("user","Date: {Date} ")])

#streamlit framework
st.title("Enter a date before the year 2025")
input_text = st.text_input("Enter the Date (e.g., 15 August 1947)")

#openAI LLM
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")


if input_text:
    # Format + run prompt directly
    chain = prompt | llm
    time.sleep(5)  # wait between queries to avoid 429
    response = chain.invoke({"Date": input_text})
    
    st.write(response.content)

