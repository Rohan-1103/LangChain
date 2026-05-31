from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_groq import ChatGroq

from dotenv import load_dotenv
import asyncio
import os

# Load .env
load_dotenv()


async def main():

    # Load API Key
    groq_key = os.getenv("GROQ_API_KEY")

    if not groq_key:
        raise ValueError("GROQ_API_KEY not found")

    os.environ["GROQ_API_KEY"] = groq_key

    # Multi MCP Server Client
    client = MultiServerMCPClient(
        {
            # STDIO Server
            "math": {
                "command": "python",
                "args": ["7-mathserver.py"],
                "transport": "stdio",
            },

            # HTTP Server
            "weather": {
                "url": "http://127.0.0.1:8000/mcp",
                "transport": "streamable_http",
            }
        }
    )

    # Load tools from both servers
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

    # Two messages
    response = await agent.ainvoke(
        {
            "messages": [

                # Message 1 -> Math MCP Server
                {
                    "role": "user",
                    "content": "What is (3 + 5) * 12?"
                },

                # Message 2 -> Weather MCP Server
                {
                    "role": "user",
                    "content": "What is the weather in Mumbai?"
                }
            ]
        }
    )

    # Print final response
    print("\nFinal Response:\n")
    print(response["messages"][-1].content)


# Run application
asyncio.run(main())