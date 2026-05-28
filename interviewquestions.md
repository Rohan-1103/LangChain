
# Common AI Engineer Interview Questions

## 1. What is the difference between an LLM and an AI Agent?

### Answer

An LLM mainly generates text based on input prompts, while an AI agent can reason, use tools, maintain memory, and perform actions autonomously.

---

## 2. What is context window in LLMs?

### Answer

The context window is the maximum number of tokens an LLM can process in a single interaction, including both input and output tokens.

---

## 3. Why is streaming important in AI applications?

### Answer

Streaming improves responsiveness by displaying tokens progressively, reducing perceived latency and improving user experience.

---

## 4. What is the role of a System Message?

### Answer

A system message defines the model’s behavior, tone, rules, and instructions before user interaction begins.

---

## 5. What is batching and why is it useful?

### Answer

Batching processes multiple requests together, improving throughput, reducing latency, and lowering API costs.

---

## 6. What are tool calls in AI agents?

### Answer

Tool calls allow LLMs to interact with external systems such as APIs, databases, calculators, or search engines to perform actions beyond text generation.

---

# Most Important Interview Questions — Hidden Thinking Process in LLMs

## 1. How do chatbots hide their internal reasoning process?

### Answer

Chatbots separate internal reasoning and final output using special tokens like `</think>`. The UI filters out the reasoning part and only displays the final response to the user.

---

## 2. How do LLMs actually “think”?

### Answer

LLMs process text as tokens and predict the next most probable token using patterns learned during training through the Transformer architecture.

---

## 3. What is the Attention Mechanism in LLMs?

### Answer

Attention helps the model determine which words or tokens are most important relative to each other while generating responses.

---

## 4. What are attention maps?

### Answer

Attention maps visualize how strongly one token focuses on other tokens during processing.

---

## 5. What are logits in LLMs?

### Answer

Logits are raw prediction scores generated before converting them into probabilities for next-token prediction.

---

## 6. What are embedding vectors?

### Answer

Embedding vectors are numerical representations of words in high-dimensional space where semantically similar words are positioned closely together.

---

## 7. What are hidden states in LLMs?

### Answer

Hidden states are intermediate internal representations generated at different neural network layers during processing.

---

## 8. What is mechanistic interpretability?

### Answer

Mechanistic interpretability is the study of understanding how internal neural network components perform reasoning and decision-making.

---

## 9. What is chain-of-thought reasoning?

### Answer

Chain-of-thought reasoning is the step-by-step internal reasoning process an LLM performs before generating the final answer.

---

## 10. Which libraries are commonly used to trace LLM internals?

### Answer

Popular libraries include:

* TransformerLens
* Hugging Face Transformers
* PyTorch hooks

---

# Best Interview One-Liner

> "LLMs internally process tokens using transformer-based attention mechanisms, generating hidden representations and probability distributions before producing the final filtered response."


# Recruiter Tips for Interviews

## Important Keywords to Use

* Transformer Architecture
* Attention Mechanism
* Tokenization
* Context Window
* Tool Calling
* Function Calling
* Retrieval-Augmented Generation (RAG)
* Autonomous Agents
* Prompt Engineering
* Streaming Responses

## What Interviewers Look For

* Clear understanding of fundamentals
* Ability to explain concepts simply
* Practical implementation knowledge
* Updated syntax familiarity
* Real-world use cases
* System design understanding
