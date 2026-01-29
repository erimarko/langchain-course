from dotenv import load_dotenv
load_dotenv()
import traceback
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from tavily import TavilyClient
from datetime import datetime, timedelta
tavily_client = TavilyClient()
search_response = tavily_client.search("Who is Leo Messi?")

# print(search_response)

extract_response = tavily_client.extract([
    "https://en.wikipedia.org/wiki/Lionel_Messi",
    "https://www.fcbarcelona.com/en/",
    "https://www.intermiamicf.com/news/"
])

topics = [
    "US Politics", # Fill in topic 1
    "Global Economy", # Fill in topic 2
    "Tech"  # Fill in topic 3
]
conTEXT = []
for topic in topics:
    # skip empty topics early and produce an empty results list
    if not topic:
        conTEXT.append({"topic": topic, "RESULTS": []})
        continue

    search_response = tavily_client.search(topic, topic="news", time_range="day")

    # support both a direct iterable response or a dict with a "results" key
    if isinstance(search_response, dict) and "results" in search_response:
        items = search_response["results"]
    else:
        items = search_response or []

    results_list = []
    for result in items:
        # use .get to avoid KeyError if a field is missing
        results_list.append({
            "url": result.get("url"),
            "title": result.get("title"),
            "snippet": result.get("content")
        })

    conTEXT.append({
        "topic": topic,
        "RESULTS": results_list
    })
gpt_5_response = ChatOpenAI(model="gpt-5", temperature=0)
prompt = """
    You are a Journalist agent.

    - Generate a daily news digest. Today's date is {date}.
    - Use only the following sources to get accurate information for each topic and write a short article about it:
      {context}.
    """
formatted_prompt = prompt.format(context=conTEXT, date=datetime.now().strftime("%Y-%m-%d"))

# Invoke the model with the formatted prompt and print the response content.
response = gpt_5_response.invoke(formatted_prompt)
print(response.content)
