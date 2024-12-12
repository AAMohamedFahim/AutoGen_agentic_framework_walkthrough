
# Conversable Agent

The `ConversableAgent` class, part of the `autogen` package, enables seamless conversational interactions with various language models (LLMs). It allows you to create an agent that can generate responses based on user inputs. 


This class is perfect for building chatbots or virtual assistants that leverage multiple AI models for intelligent, context-driven conversations.

## Chapter Content

- [1. Conversation History ](#conversation-history)
- [2. Conversation Between Multiple Agent](#conversation-between-multiple-agent)
- [3. Termination condition](#terminate-conversation-based-on-condition)

---


## Conversation History

### **Importing ConversableAgent Package**

To begin, we import the required `ConversableAgent` and the `config_list_from_dotenv` function.

```python
from autogen import ConversableAgent, config_list_from_dotenv
```

### **Model API Key Mapping**

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

### **Loading Configuration List**

Next, we load the configuration list by reading the `.env` file. This contains the environment variables required for connecting to the APIs.

```python
config_list = config_list_from_dotenv(
    dotenv_file_path=".env", 
    model_api_key_map=model_api_key_map,
)
```

> **Note:** The `.env` file should contain the necessary environment variables (e.g., `AZURE_API`, `GROQ_API`) with appropriate values.

### **Initializing ConversableAgent**

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

### **Testing the ConversableAgent**

To check if the agent is functioning correctly, we can print its type and interact with it using a simple conversation loop. The agent generates replies based on the user input.

```python
print(type(agent))  
```

### Output:
```shell
<class 'autogen.agentchat.conversable_agent.ConversableAgent'>
```

### **Conversational Interaction**

Finally, we use the agent to simulate a conversation. The user inputs a prompt, and the agent generates a response. The conversation continues with a second prompt.

```python
prompt = input("User: ")
print("Agent: ", agent.generate_reply(messages=[{"role": "user", "content": prompt}]))

prompt = input("User: ")
print("Agent: ", agent.generate_reply(messages=[{"role": "user", "content": prompt}]))
```
### Output:
```shell
User: tell me a joke  
agent: Why don't skeletons fight each other?  
        They don't have the guts!
User: what is my previous question  
agent: I don't have the ability to recall previous interactions or questions once the conversation ends. However, I can help with any new questions you have or any topics you'd like to discuss! What can I assist you with today?
```
**Note** :`Convertation is not stored in default we will see how to store convertaition in upcoming chapters`

## Conversation Between Multiple Agent

### Same Setup: 
```python
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

config_list = config_list_from_dotenv(
    dotenv_file_path=".env", 
    model_api_key_map=model_api_key_map,
)
```

### Customer Agent
Defines an agent representing a customer in a supermarket scenario.

```python
customer = ConversableAgent(
    name = "customer",
    system_message="you are customer going to supermarket",
    llm_config=config_list[0], 
    human_input_mode="NEVER"
)
```


### Shopkeeper Agent
Defines an agent representing a shopkeeper in the supermarket scenario.

```python
shopkeeper = ConversableAgent(
    name = "shopkeeper",
    system_message="you are shopkeeper of supermarket",
    llm_config=config_list[0], 
    human_input_mode="NEVER"
)
```

### Parameters:
- **name**: Identifier for the agent. Here, it is `"shopkeeper"` or `"customer"`.
- **system_message**: A brief description defining the agent's role and behavior. This agent is a shopkeeper in a supermarket.
- **llm_config**: Configuration for the underlying large language model (LLM). `config_list[0]` is passed here.
- **human_input_mode**: Defines how the agent receives inputs. `"NEVER"` indicates the agent doesn't accept human input.

---

### Initiating Conversation
The `shopkeeper` agent initiates a conversation with the `customer` agent.

```python
chat_result = shopkeeper.initiate_chat(
    recipient=customer,
    message="what do you looking for",
    max_turns=2
)
```

### Parameters:
- **recipient**: Specifies the target agent for the message. Here, it is the `customer` agent.
- **message**: The initial message sent by the initiating agent. Here, the message is `"what do you looking for"`.
- **max_turns**: Limits the number of interaction turns. Here, it is set to `2`.

### Output:
```shell

shopkeeper (to customer):

what do you looking for

--------------------------------------------------------------------------------
customer (to shopkeeper):

I'm looking for some fresh fruits and vegetables, as well as some snacks for the week. Do you have any recommendations?

--------------------------------------------------------------------------------
shopkeeper (to customer):

Absolutely! For fresh fruits, I recommend our seasonal options like strawberries, blueberries, and apples. They are both delicious and nutritious. As for vegetables, you might want to try our organic spinach, bell peppers, and cherry tomatoes—they're great for salads or cooking.

For snacks, we have a variety of options! Our mixed nuts and granola bars are popular choices. If you're looking for something crunchy, you might enjoy our whole grain crackers or popcorn. Do you have any specific preferences or dietary restrictions I should keep in mind?

--------------------------------------------------------------------------------
customer (to shopkeeper):

:customer  
I love all those options! I don't have any dietary restrictions, but I'm trying to cut back on sugar. Do you have any low-sugar snack alternatives?

--------------------------------------------------------------------------------
```

### Analyzing Chat Results

### Printing Chat History
To view the conversation history, use the following code:

```python
import pprint

pprint.pprint(chat_result.chat_history)
```

### Explanation:
- **chat_history**: Stores the chronological list of messages exchanged between agents, including roles and content.
- **Output:**

```plaintext
[{'content': 'what do you looking for',
  'name': 'shopkeeper',
  'role': 'assistant'},
 {'content': "I'm looking for some fresh fruits and vegetables, as well as "
             'some snacks for the week. Do you have any recommendations?',
  'name': 'customer',
  'role': 'user'},
 {'content': 'Absolutely! For fresh fruits, I recommend our seasonal options '
             'like strawberries, blueberries, and apples. They are both '
             'delicious and nutritious. As for vegetables, you might want to '
             'try our organic spinach, bell peppers, and cherry '
             "tomatoes—they're great for salads or cooking.\n"
             '\n'
             'For snacks, we have a variety of options! Our mixed nuts and '
             "granola bars are popular choices. If you're looking for "
             'something crunchy, you might enjoy our whole grain crackers or '
             'popcorn. Do you have any specific preferences or dietary '
             'restrictions I should keep in mind?',
  'name': 'shopkeeper',
  'role': 'assistant'},
 {'content': ':customer  \n'
             "I love all those options! I don't have any dietary restrictions, "
             "but I'm trying to cut back on sugar. Do you have any low-sugar "
             'snack alternatives?',
  'name': 'customer',
  'role': 'user'}]
```

---

### Printing Cost Information
To view the cost metrics of the interaction:

```python
pprint.pprint(chat_result.cost)
```

### Explanation:
- **cost**: Provides cost details related to token usage in the chat.
- **Output:**

```plaintext
{'usage_excluding_cached_inference': {'total_cost': 0},
 'usage_including_cached_inference': {'gpt-4o-mini': {'completion_tokens': 165,
                                                      'cost': 0.00013619999999999998,
                                                      'prompt_tokens': 248,
                                                      'total_tokens': 413},
                                      'total_cost': 0.00013619999999999998}}
```

---

### Printing Summary
To extract and print the final summary or the last agent's message:

```python
pprint.pprint(chat_result.summary)
```

### Explanation:
- **summary**: Provides a concise summary or extracts the most recent message from the conversation.
- **Output:**

```plaintext
(':customer  \n'
 "I love all those options! I don't have any dietary restrictions, but I'm "
 'trying to cut back on sugar. Do you have any low-sugar snack alternatives?')
```

### Summarization Method

```python  
    new_chat_result = shopkeeper.initiate_chat(
    recipient=customer,
    message="what do you looking for",
    max_turns=2,
    summary_method="reflection_with_llm",  # default "last_msg"
)

pprint.pprint(new_chat_result.summary)

```
- **summary**: Provides a concise summary of the convertation.
- **Output** : 
```plaintext
('The customer is looking for fresh fruits and vegetables, as well as snacks. '
 'The shopkeeper recommends seasonal fruits like strawberries and apples, '
 'organic vegetables like spinach and bell peppers, and snack options '
 'including mixed nuts and granola bars. The customer is interested in '
 'low-sugar snack alternatives to help reduce sugar intake.')`
```

**If we make agents by mentioning turn limit is not a right way to do in all situation so we have a `is_termination` to terminate based on the condition let see about that**

## Terminate conversation based on condition


### Same Setup: 
```python
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

config_list = config_list_from_dotenv(
    dotenv_file_path=".env", 
    model_api_key_map=model_api_key_map,
)
```


### Defining the Customer Agent with modified prompt
The customer agent is designed to behave as a supermarket customer with a predefined end note.

```python
customer = ConversableAgent(
    name = "customer",
    system_message="You are a customer going to a supermarket."
    "Once you complete your purchase, you should exactly say in all lowercase without any punctuation or symbols: 'thank you for your service'",
    llm_config=config_list[0], 
    human_input_mode="NEVER",
)
```

### Defining the Shopkeeper Agent with termination condition and modified prompt
The shopkeeper agent is designed to respond to the customer and terminate the chat upon receiving the end note.

```python
shopkeeper = ConversableAgent(
    name = "shopkeeper",
    system_message="You are the shopkeeper of a supermarket."
    "If a customer says exactly 'Thank you for your service', you should say exactly 'Thank you, visit again.'",
    llm_config=config_list[0], 
    human_input_mode="NEVER",
    is_termination_msg=lambda msg: "thank you for your service" in msg["content"]
)
```

### Explanation:
- **is_termination_msg**: It returns True if the condition is satisfies else False. (Terminates the conversation if the customer’s message contains "thank you for your service".)

---

### Initiating the Chat
The shopkeeper initiates the conversation with the customer by asking what they want to find.

```python
chat_result = shopkeeper.initiate_chat(
    recipient=customer,
    message="What do you want to find?",
)
```

### Continuing the Conversation
The customer continues the interaction by asking a follow-up question. The termination condition remains unchanged.

```python
customer.send(message="What did I ask you previously?", recipient=shopkeeper)
```

### Explanation:
- **send**: Sends a message from the customer to the shopkeeper.
- **message**: The follow-up question from the customer.
- **recipient**: Specifies the shopkeeper as the recipient.

---

### Termination Condition
- The conversation will terminate when the customer says exactly "thank you for your service" in lowercase, without punctuation or symbols.
- The shopkeeper will respond with "Thank you, visit again." before the conversation ends.

---

This setup ensures a realistic and controlled interaction between agents with clear termination criteria.

## End Note

This chapter demonstrated how to define agents with termination conditions and manage their interactions using the ConversableAgent framework. The next chapter will delve into advanced interaction scenarios and dynamic behavior customization.

### Continue Learning
- **Previous Chapter**: [Chapter 1: Autogen and LLM Setup](1.Autogen and LLM Setup)
- **Next Chapter**: [Chapter 3: Advanced Interaction Scenarios](#)

### Code Reference
- **Code for This Chapter**: [Chapter 2 Code](#)
