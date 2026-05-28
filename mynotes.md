# AI Engineering Fundamentals for Interviews

# What Exactly Are Agents?

## Definition

Agents are AI systems capable of reasoning, making decisions, and taking actions autonomously to achieve a goal.

Unlike traditional LLM applications that only generate text, agents can:

* Think step-by-step
* Use tools/APIs
* Access external data
* Maintain memory
* Execute actions based on goals

## Core Components of an AI Agent

1. **LLM (Brain)**
   Performs reasoning and language understanding.

2. **Tools**
   External functions/APIs such as:

   * Search engines
   * Databases
   * Python execution
   * Web APIs

3. **Memory**
   Stores previous interactions and context.

4. **Reasoning Engine**
   Decides:

   * Which tool to use
   * What action to take
   * What response to generate

## Example

User: "Book me the cheapest flight to Delhi tomorrow."

Agent Workflow:

1. Understands intent
2. Searches flight APIs
3. Compares prices
4. Selects best option
5. Returns result

## Interview One-Liner

> "An AI agent is an autonomous system powered by an LLM that can reason, use tools, and take actions to accomplish tasks."

---

# What Are LLMs?

## Definition

LLMs (Large Language Models) are deep learning models trained on massive amounts of text and code data to understand, generate, and manipulate human language.

They are primarily built using the **Transformer architecture**.

## Popular LLMs

* GPT-4o
* Claude
* Gemini
* Llama
* Mistral

## Capabilities

* Text generation
* Summarization
* Translation
* Question answering
* Code generation
* Reasoning
* Tool calling

## Interview One-Liner

> "LLMs are transformer-based neural networks trained on large-scale datasets to perform natural language understanding and generation tasks."

---

# Main Task of an LLM

## Core Idea

LLMs take an input and generate the most probable next tokens as output.

## Example

Input:

```text
What is the capital of France?
```

Output:

```text
Paris
```

## Technical Explanation

LLMs work using:

* Tokenization
* Attention mechanisms
* Probability prediction

The model predicts the next token repeatedly until completion.

## Interview One-Liner

> "The primary task of an LLM is next-token prediction based on learned language patterns."

---

# Knowledge Cutoff Date

## Definition

The knowledge cutoff date is the point in time after which the model has no built-in knowledge of events.

## Example

If the cutoff is:

```text
June 2024
```

The model may not know:

* New company launches
* Latest frameworks
* Current events after that date

## Important Point

Models can overcome this limitation using:

* Web search
* RAG (Retrieval-Augmented Generation)
* External APIs

## Interview One-Liner

> "Knowledge cutoff refers to the last date included in the model’s training data."

---

# Context in LLMs

## Definition

Context is the information provided to the model during inference.

It helps the model generate relevant responses.

## Types of Context

* User prompts
* Conversation history
* Retrieved documents
* System instructions

## Example

```text
User: My name is Rohan.
User: What is my name?
```

The model uses previous conversation as context.

## Context Window

The maximum number of tokens the model can process at once.

Example:

* 8K
* 32K
* 128K tokens

## Interview One-Liner

> "Context is the input information available to the model while generating responses."

---

# Streaming

## Definition

Streaming means generating output token-by-token in real time instead of waiting for the full response.

## Benefits

* Better user experience
* Lower perceived latency
* Useful for chat applications

## Updated Python Example (LangChain)

```python
from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model="gpt-4o-mini",
    streaming=True
)

for chunk in model.stream("Explain AI agents"):
    print(chunk.content, end="")
```

## Interview One-Liner

> "Streaming allows incremental token generation for faster and more interactive responses."

---

# Batch Processing

## Definition

Batching means sending multiple independent requests together for parallel processing.

## Benefits

* Faster execution
* Lower API cost
* Better throughput

## Updated Example

```python
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o-mini")

responses = model.batch([
    "What is AI?",
    "What is ML?",
    "What is Deep Learning?"
])

print(responses)
```

## Interview One-Liner

> "Batching improves efficiency by processing multiple requests simultaneously."

---

# Max Concurrency

## Definition

Max concurrency defines the maximum number of parallel operations/tasks executed simultaneously.

## Usage

Used in:

* Async processing
* Batch execution
* Agent workflows

## Example

```python
from langchain_core.runnables import RunnableConfig

config = RunnableConfig(max_concurrency=5)
```

## Why Important?

Prevents:

* API rate limit errors
* Memory overload
* Resource exhaustion

## Interview One-Liner

> "Max concurrency controls how many tasks run in parallel to optimize performance and resource usage."

---

# Messages in LangChain

## Definition

Messages are structured objects representing conversation context between users and LLMs.

## Message Components

1. Role
2. Content
3. Metadata

## Why Important?

Messages enable:

* Chat memory
* Multi-turn conversations
* Tool calling
* Structured interactions

---

# Types of Messages

## 1. System Message

### Purpose

Defines model behavior and instructions.

### Example

```python
from langchain_core.messages import SystemMessage

SystemMessage(
    content="You are an AI interviewer."
)
```

### Use Cases

* Setting tone
* Defining rules
* Restricting behavior

---

## 2. Human Message

### Purpose

Represents user input.

### Example

```python
from langchain_core.messages import HumanMessage

HumanMessage(
    content="Explain transformers."
)
```

---

## 3. AI Message

### Purpose

Represents model-generated output.

### Example

```python
from langchain_core.messages import AIMessage

AIMessage(
    content="Transformers are deep learning architectures..."
)
```

---

## 4. Tool Message

### Purpose

Stores tool execution results returned back to the model.

### Example

```python
from langchain_core.messages import ToolMessage

ToolMessage(
    content="Weather is 28°C",
    tool_call_id="weather_001"
)
```

---

# Text Prompts

## Definition

Simple string-based prompts given directly to the model.

## Best For

* Single tasks
* Simple generation
* Minimal complexity

## Example

```python
response = model.invoke(
    "Explain Retrieval-Augmented Generation"
)
```

## Interview One-Liner

> "Text prompts are direct string inputs used for simple standalone interactions."

---

# Message Prompts

## Definition

Structured prompts using multiple message objects.

## Advantages

* Maintains conversation history
* Supports roles
* Better control over model behavior

## Example

```python
from langchain_core.messages import (
    SystemMessage,
    HumanMessage
)

messages = [
    SystemMessage(
        content="You are an AI tutor."
    ),
    HumanMessage(
        content="Explain vector databases."
    )
]

response = model.invoke(messages)
```

## Interview One-Liner

> "Message prompts provide structured conversational context using role-based messages."

---