from autogen import ConversableAgent, config_list_from_dotenv
import pprint 

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
    dotenv_file_path=".env", 
    model_api_key_map=model_api_key_map,
)

customer = ConversableAgent(
    name = "customer",
    system_message="you are customer going to supermarket",
    llm_config=config_list[0], 
    human_input_mode="NEVER"
)

shopkeeper = ConversableAgent(
    name = "shopkeeper",
    system_message="you are shopkeeper of supermarket",
    llm_config=config_list[0], 
    human_input_mode="NEVER"
)

chat_result = shopkeeper.initiate_chat(
    recipient=customer,
    message="what do you looking for",
    max_turns=2
)


import pprint

pprint.pprint(chat_result.chat_history)

pprint.pprint(chat_result.cost)

pprint.pprint(chat_result.summary)

new_chat_result = shopkeeper.initiate_chat(
    recipient=customer,
    message="what do you looking for",
    max_turns=2,
    summary_method="reflection_with_llm",  # default "last_msg"
)

pprint.pprint(new_chat_result.summary)