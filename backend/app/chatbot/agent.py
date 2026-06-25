from app.chatbot.llm import local_model
from app.chatbot.tools import TOOLS
from app.chatbot.prompt import prompt
from langchain.agents import AgentExecutor, create_tool_calling_agent

llm = local_model()
binder = create_tool_calling_agent( llm, TOOLS, prompt)

agent = AgentExecutor(
    agent=binder,
    tools=TOOLS,
    verbose=True
)

# test 
# response  = agent.invoke({"input" : "What is the the relation between items, customers and sales orders?"})
# print(response["output"])