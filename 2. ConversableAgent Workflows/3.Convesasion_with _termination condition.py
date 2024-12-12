from autogen import ConversableAgent, config_list_from_dotenv

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
    system_message="You are a customer going to a supermarket."
    "Once you complete your purchase, you should exactly say in all lowercase without any punctuation or symbols: 'thank you for your service'",
    llm_config=config_list[0], 
    human_input_mode="NEVER",
)

shopkeeper = ConversableAgent(
    name = "shopkeeper",
    system_message="You are the shopkeeper of a supermarket."
    "If a customer says exactly 'Thank you for your service', you should say exactly 'Thank you, visit again.'",
    llm_config=config_list[0], 
    human_input_mode="NEVER",
    is_termination_msg=lambda msg: "thank you for your service" in msg["content"]
)

chat_result = shopkeeper.initiate_chat(
    recipient=customer,
    message="What do you want to find?",

)

customer.send(message="What did I ask you previously?",recipient=shopkeeper)