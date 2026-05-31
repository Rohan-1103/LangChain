from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_groq import ChatGroq

from dotenv import load_dotenv
import asyncio
import os

# Load .env
load_dotenv()


async def main():

    # Get API Key
    groq_key = os.getenv("GROQ_API_KEY")

    if not groq_key:
        raise ValueError("GROQ_API_KEY not found in .env file")

    os.environ["GROQ_API_KEY"] = groq_key

    # MCP Client
    client = MultiServerMCPClient(
        {
            # Math MCP Server (STDIO)
            "math": {
                "command": "python",
                "args": ["7-mathserver.py"],
                "transport": "stdio",
            },

            # Weather MCP Server (HTTP)
            "weather": {
                "url": "http://127.0.0.1:8000/mcp",
                "transport": "streamable_http",
            }
        }
    )

    # Load tools from MCP servers
    tools = await client.get_tools()

    # LLM
    model = ChatGroq(
        model="llama-3.1-8b-instant"
    )

    # Create Agent
    agent = create_agent(
        model=model,
        tools=tools
    )

    # Query
    response = await agent.ainvoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What is the weather in Mumbai and what is (3 + 5) x 12?"
                }
            ]
        }
    )

    # Print final answer
    print("\nFinal Response:\n")
    print(response["messages"][-1].content)


# Run app
asyncio.run(main())