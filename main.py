from dotenv import load_dotenv
load_dotenv()
import traceback
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from tavily import TavilyClient
tavily = TavilyClient()
@tool
def search(query: str) -> str:
    """Tool that searched over internet. 
    Args:
        query: The query to search for.
        Returns:
        The search results."""
    print(f"Searching for {query}")
    # return "Tokyo weather is sunny"
    return tavily.search(query=query)
llm = ChatOpenAI(model="gpt-5", temperature=0)
tools = [search]
agent = create_agent(
    llm,
    tools=tools,
    system_prompt="You are a helpful assistant.",
)
def main():
    print("Hello from longchain-course!")
    # result = agent.invoke({"messages": [HumanMessage(content="What is the weather in Tokyo?")]})
    try:
        result = agent.invoke({"messages": [HumanMessage(content="search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details?")]})
        print(result)
    
    except Exception as e:
        print(f"Error occurred: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    main()    
   
