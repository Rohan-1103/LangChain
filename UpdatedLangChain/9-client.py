from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()

import asyncio
import sys
import os


async def main():
    repo_dir = os.path.dirname(__file__)
    math_script = os.path.join(repo_dir, "7-mathserver.py")
    client = MultiServerMCPClient(
        {
            "math":{
                "command": sys.executable,
                "args":[math_script],
                "transport": "stdio",
            },
            "weather":{
                "url": "http://127.0.0.1:8000/mcp",
                "transport": "streamable_http",  
            }       
        }
    )
    
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
    
    tools = await client.get_tools()
    model = ChatGroq(model="llama-3.1-8b-instant", temperature=0.0)
    agent = create_agent(model=model, tools=tools)
    
    math_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "What is (3 + 5) x 12?"}]})
    print("Math response: ", math_response['messages'][-1].content)

asyncio.run(main())