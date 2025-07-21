from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from config.constants import GEMINI_MODEL
from dotenv import load_dotenv
import os
load_dotenv()



def get_model_client():
    gemini_model_client = OpenAIChatCompletionClient(
        model=GEMINI_MODEL,
        api_key=os.getenv('GOOGLE_API_KEY'),
    )
    
    return gemini_model_client