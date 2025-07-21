from autogen_core.models import UserMessage
from autogen_ext.models.ollama import OllamaChatCompletionClient
from autogen_agentchat.agents import AssistantAgent


# Assuming your Ollama server is running locally on port 11434.
ollama_model_client = OllamaChatCompletionClient(model="llama3.2")


assistant = AssistantAgent(name = "ollama_agent" , 
                           model_client=ollama_model_client)

