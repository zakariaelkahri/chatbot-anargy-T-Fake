from app.chatbot.llm import local_model, gemini_model
from app.chatbot.tools import TOOLS
from app.chatbot.prompt import prompt
from langchain.agents import AgentExecutor, create_tool_calling_agent

llm = local_model()
binder = create_tool_calling_agent( llm, TOOLS,prompt)

agent = AgentExecutor(
    agent=binder,
    tools=TOOLS,
    # verbose=True
)

# # test 
# response  = agent.invoke({"input" : "What is the the list of available items?"})
# print(response["output"])


# # 1. Initialize the LLM (Gemini handles structured tool binding natively)
# llm = gemini_model()

# # 2. Create the tool calling agent (Make sure 'prompt' has agent_scratchpad)
# binder = create_tool_calling_agent(llm=llm, tools=TOOLS, prompt=prompt)

# # 3. Create the executor
# agent = AgentExecutor(
#     agent=binder,
#     tools=TOOLS,
#     verbose=True # Highly recommended during development to see tool selection!
# )