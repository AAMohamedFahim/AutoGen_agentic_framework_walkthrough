
# Conversable Agent

The `ConversableAgent` class, part of the `autogen` package, enables seamless conversational interactions with various language models (LLMs). It allows you to create an agent that can generate responses based on user inputs. 


This class is perfect for building chatbots or virtual assistants that leverage multiple AI models for intelligent, context-driven conversations.

## Chapter Content

- [1. Conversation History ](#conversation-history)

---


## Conversation History

#### **Importing ConversableAgent Package**

To begin, we import the required `ConversableAgent` and the `config_list_from_dotenv` function.

```python
from autogen import ConversableAgent, config_list_from_dotenv
```

#### **Model API Key Mapping**

This dictionary defines the mapping between the model names and their respective API credentials, including keys and endpoints.

```python
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
```

#### **Loading Configuration List**

Next, we load the configuration list by reading the `.env` file. This contains the environment variables required for connecting to the APIs.

```python
config_list = config_list_from_dotenv(
    dotenv_file_path=".env", 
    model_api_key_map=model_api_key_map,
)
```

> **Note:** The `.env` file should contain the necessary environment variables (e.g., `AZURE_API`, `GROQ_API`) with appropriate values.

#### **Initializing ConversableAgent**

We initialize the `ConversableAgent` with the following parameters:
- `name`: The name of the agent.
- `llm_config`: The configuration to use, which is fetched from the `config_list`. The `config_list[0]` refers to the GPT-4o-mini configuration, and `config_list[1]` would be for Llama-3.2.
- `human_input_mode`: Set to `"NEVER"` to disable human input mode.

```python
agent = ConversableAgent(
    name="one",
    llm_config=config_list[0],  # 0 for gpt-4o-mini and 1 for llama3.2
    human_input_mode="NEVER"
)
```

#### **Testing the ConversableAgent**

To check if the agent is functioning correctly, we can print its type and interact with it using a simple conversation loop. The agent generates replies based on the user input.

```python
print(type(agent))  
```

#### Output:
```shell
<class 'autogen.agentchat.conversable_agent.ConversableAgent'>
```

#### **Conversational Interaction**

Finally, we use the agent to simulate a conversation. The user inputs a prompt, and the agent generates a response. The conversation continues with a second prompt.

```python
prompt = input("User: ")
print("Agent: ", agent.generate_reply(messages=[{"role": "user", "content": prompt}]))

prompt = input("User: ")
print("Agent: ", agent.generate_reply(messages=[{"role": "user", "content": prompt}]))
```
#### Output:
```shell
User: tell me a joke  
agent: Why don't skeletons fight each other?  
        They don't have the guts!
User: what is my previous question  
agent: I don't have the ability to recall previous interactions or questions once the conversation ends. However, I can help with any new questions you have or any topics you'd like to discuss! What can I assist you with today?
```
**Note** :`Convertation is not stored in default we will see how to store convertaition in upcoming chapters`