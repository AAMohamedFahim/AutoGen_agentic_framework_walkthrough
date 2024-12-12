"""importing conversable agent package"""

from autogen import ConversableAgent, config_list_from_dotenv

"""model mapping"""
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


"""adding config list"""
config_list = config_list_from_dotenv(
    dotenv_file_path=".env", 
    model_api_key_map=model_api_key_map,
)

# print(config_list)
"""explain each parameter inside Conversableagent"""
agent = ConversableAgent(
    name = "one",
    llm_config=config_list[0], # 0 for gpt-4o-mini and 1 for llama3.2
    human_input_mode="NEVER"
)

print(type(agent))
"""output it returns : <class 'autogen.agentchat.conversable_agent.ConversableAgent'>""" \
    
"""chechking does agent stores convertation history"""
prompt = input("User :")
print("agent : ",agent.generate_reply(messages=[{"role":"user","content":prompt}]))
prompt = input("User :")
print("agent : ",agent.generate_reply(messages=[{"role":"user","content":prompt}]))




"""create me a readme file based on this code snippet follow the instructuon provided in the codes command and make it as a seperate blocks of code baed on the commande given"""