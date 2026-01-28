from typing import List
from pydantic import BaseModel, Field
from dotenv import load_dotenv
load_dotenv()
import traceback
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
"""
from tavily import TavilyClient
tavily = TavilyClient()
"""
class Source(BaseModel):
    """Schema for a source used by the agent"""
    url: str = Field(description="The URL of the source")
    
class AgentResponse(BaseModel):
    """Schema for agent response with answer and sources"""
    answer: str = Field(description="Thr agent's answer to the query")
    sources: List[Source] = Field(
        default_factory=list, description="List of sources used to generate the answer"
    )    

llm = ChatOpenAI(model="gpt-5", temperature=0)
tools = [TavilySearch()]
agent = create_agent(
    llm,
    tools=tools,
    response_format=AgentResponse
)
def main():
    print("Hello from longchain-course!")
    # result = agent.invoke({"messages": [HumanMessage(content="What is the weather in Tokyo?")]})
    try:
        result = agent.invoke({"messages": HumanMessage(content="search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details?")})
        print(result)
    
    except Exception as e:
        print(f"Error occurred: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    main()    
   
