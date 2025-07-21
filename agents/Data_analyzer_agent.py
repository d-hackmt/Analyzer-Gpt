from autogen_agentchat.agents import AssistantAgent
from prompts.data_analyzer_prompt import DATA_ANALYZER_SYSTEM_MESSAGE

def getDataAnalyzerAgent(model_client):
    
    data_analyzer_Agent = AssistantAgent(
        name = "Data_analyzer_agent",
        model_client=model_client,
        description="An agent that solves data analysis problems and gives codes as well",
        system_message=DATA_ANALYZER_SYSTEM_MESSAGE
    )
    
    return data_analyzer_Agent