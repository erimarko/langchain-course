from dotenv import load_dotenv
load_dotenv()
import traceback
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from tavily import TavilyClient
tavily_client = TavilyClient()
search_response = tavily_client.search("Who is Leo Messi?")

# print(search_response)

extract_response = tavily_client.extract([
    "https://en.wikipedia.org/wiki/Lionel_Messi",
    "https://www.fcbarcelona.com/en/",
    "https://www.intermiamicf.com/news/"
])

print(extract_response)