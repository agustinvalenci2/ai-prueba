from langchain_openai import OpenAI
from langchain.agents import initialize_agent, AgentType
import os
from langchain_community.agent_toolkits.load_tools import load_tools
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()



# Initialize Langchain Agent
def get_langchain_response(user_input: str,prev_messages):
    llm = OpenAI(temperature=0)
    tools = load_tools(["openweathermap-api"], llm=llm)
    agent_chain = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
        verbose=False,
        handle_parsing_errors=True
    )
    if isinstance(prev_messages, list) and all(isinstance(msg, str) for msg in prev_messages):
        # Si `prev_messages` es una lista de strings, convertimos los pares en formato estructurado
        prev_messages = [{"role": "user" if i % 2 == 0 else "assistant", "content": msg} for i, msg in enumerate(prev_messages)]
    print("prev msg",prev_messages)
    return agent_chain.run({"input": user_input, "chat_history":prev_messages})

