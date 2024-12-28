# AutoGen Framework

This repository demonstrates the use of the AutoGen Framework to set up and interact with Conversable Agents using different LLM configurations. The setup includes integrations for Azure OpenAI and GROQ APIs. Users can choose to use either Azure, GROQ, or both based on their requirements.

## Features

- **Multiple API Integrations**: Configure models for Azure OpenAI and GROQ.
- **Conversable Agent**: Create agents that generate conversational replies.
- **Environment Variable Support**: Load API keys and configuration settings from a `.env` file.

## Prerequisites

- Python 3.8+
- Required libraries: `autogen`, `dotenv`
- Access to Azure OpenAI and/or GROQ API keys

## Setup Options

You can configure the framework in three different ways:

### Option 1: Using GROQ Only

1. Configure your `.env` file:

    ```env
    GROQ_API=<your_groq_api_key>
    ```

2. Define your model API map:

    ```python
    model_api_key_map = {
        "groq-model": {
            "api_key_env_var": "GROQ_API",
            "api_type": "groq",
        }
    }
    ```

3. Load configurations and create an agent:

    ```python
    config_list = config_list_from_dotenv(
        dotenv_file_path=".env", # path to .env file
        model_api_key_map=model_api_key_map,
    )

    agent = ConversableAgent(
        name="groq_agent",
        llm_config=config_list[0],
        human_input_mode="NEVER"
    )
    ```

**Note**: check path to .env if any error occured.


### Option 2: Using Azure OpenAI Only

1. Configure your `.env` file:

    ```env
    AZURE_API=<your_azure_api_key>
    AZURE_ENDPOINT=<your_azure_api_endpoint>
    AZURE_VERSION = <you-azure-version>
    ```

2. Define your model API map:

    ```python
    model_api_key_map = {
        "azure-model": {
            "api_key_env_var": "AZURE_API",
            "base_url": "AZURE_ENDPOINT",
            "api_type": "azure",
            "api_version": "AZURE_VERSION",
        }
    }
    ```

3. Load configurations and create an agent:

    ```python
    config_list = config_list_from_dotenv(
        dotenv_file_path=".env", # path to .env file
        model_api_key_map=model_api_key_map,
    )

    agent = ConversableAgent(
        name="azure_agent",
        llm_config=config_list[0],
        human_input_mode="NEVER"
    )
    ```
**Note**: check path to .env if any error occured.

### Option 3: Using Both Azure and GROQ

1. Configure your `.env` file:

    ```env
    GROQ_API=<your_groq_api_key>
    AZURE_API=<your_azure_api_key>
    AZURE_ENDPOINT=<your_azure_api_endpoint>
    AZURE_VERSION = <you-azure-version>
    ```

2. Define your model API map:

    ```python
    model_api_key_map = {
        "azure-model": {
            "api_key_env_var": "AZURE_API",
            "base_url": "AZURE_ENDPOINT",
            "api_type": "azure",
            "api_version": "AZURE_VERSION",
        },
        "groq-model": {
            "api_key_env_var": "GROQ_API",
            "api_type": "groq",
        }
    }
    ```

3. Load configurations and create an agent for each model:

    ```python
    config_list = config_list_from_dotenv(
        dotenv_file_path=".env", # path to .env file
        model_api_key_map=model_api_key_map,
    )

    azure_agent = ConversableAgent(
        name="azure_agent",
        llm_config=config_list[0], # 0th index in model map
        human_input_mode="NEVER"
    )

    groq_agent = ConversableAgent(
        name="groq_agent",
        llm_config=config_list[1], # 1th index in model map
        human_input_mode="NEVER"
    )
    ```

**Note**: check path to .env if any error occured.

## Example Output

For any configuration, the output might look like this:

```bash
[{'api_key_env_var': 'AZURE_API', 'base_url': '<azure_base_url>', 'api_type': 'azure', 'api_version': '<azure_api_version>'}, {'api_key_env_var': 'GROQ_API', 'api_type': 'groq'}]
<class 'autogen.ConversableAgent'>
Hello! How can I assist you?
```
### Continue Learning
- **Next Chapter**: [Chapter 2: Build a Conversable Agent](../2.%20ConversableAgent%20Workflows/)  
  In this chapter, we’ll build an interactive agent that not only understands user queries but also takes action, bringing your bot to life with real-time conversations.

### Code Reference
- **Code for This Chapter**: [Chapter 1 Code](./main..py)
