from autogen_agentchat.agents import CodeExecutorAgent
import asyncio 

# no need of brain , just docker

def getCodeExecuterAgent(code_executer):

    code_executer_agent = CodeExecutorAgent(
        name = "Python_code_executer",
        code_executor=code_executer
    )

    return code_executer_agent

