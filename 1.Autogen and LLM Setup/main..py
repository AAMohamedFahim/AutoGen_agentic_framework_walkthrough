from autogen import config_list_from_dotenv
from autogen import ConversableAgent

model_api_key_map = {
    "gpt-4o-mini-testing": {
        "api_key_env_var": "AZURE_API",
        "base_url": "AZURE_ENDPOINT",
        "api_type": "azure",
        "api_version": "AZURE_VERSION",
    },
    "llama-3.2-3b-preview": {
        "api_key_env_var": "GROQ_API",
        "api_type": "groq",
    }
}


config_list = config_list_from_dotenv(
    dotenv_file_path=".env",  # path to .env file
    model_api_key_map=model_api_key_map,
)

print(config_list)

agent = ConversableAgent(
    name = "one",
    llm_config=config_list[0], # 0 for gpt-4o-mini and 1 for llama3.2
    human_input_mode="NEVER"
)
print(type(agent)) 
print(agent.generate_reply(messages=[{"role":"user","content":"what is your model"}]))