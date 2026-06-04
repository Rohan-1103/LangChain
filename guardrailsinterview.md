
# Most Important Interview Questions

## 1. What are Guardrails in LangChain?

### Answer

Guardrails are middleware-based safety mechanisms that validate and control agent behavior.

---

## 2. Why are Guardrails important?

### Answer

They prevent:

* PII leakage
* Prompt injection
* Harmful outputs
* Unsafe tool execution

---

## 3. What is the difference between Deterministic and Model-Based Guardrails?

### Answer

Deterministic guardrails use predefined rules, while model-based guardrails use AI reasoning to detect violations.

---

## 4. Why are deterministic guardrails faster?

### Answer

Because they use regex and rule matching instead of additional model calls.

---

## 5. Why are model-based guardrails more powerful?

### Answer

Because they understand semantic meaning and contextual intent.

---

## 6. What is PII Detection Middleware?

### Answer

Middleware that detects and redacts personally identifiable information before processing or storage.

---

## 7. What is Human-in-the-Loop Guardrail?

### Answer

A safety mechanism that pauses execution and requires human approval before sensitive actions.

---

## 8. What is a Before-Agent Guardrail?

### Answer

It validates user inputs before the agent starts processing.

---

## 9. What is an After-Agent Guardrail?

### Answer

It validates generated responses before they reach the user.

---

## 10. Why are layered guardrails recommended in production?

### Answer

Because multiple safety layers provide stronger protection than relying on a single validation mechanism.

---

## 11. Which guardrail approach is commonly used in production?

### Answer

A hybrid approach combining deterministic and model-based guardrails.

---

## 12. Where should PII detection ideally occur?

### Answer

Before logging, storage, model invocation, and output delivery.

---

# Best Interview One-Liner

> "Guardrails are middleware-based safety layers that protect AI systems from harmful inputs, unsafe outputs, prompt injections, PII leakage, and policy violations while ensuring compliance and reliability."


# Most Important Interview Questions

## 1. What are the four PII handling strategies?

### Answer

* Redact
* Mask
* Hash
* Block

---

## 2. Difference between Redact and Mask?

### Answer

Redaction completely removes information, while masking preserves partial visibility.

---

## 3. Why is Hashing useful?

### Answer

Hashing enables anonymous tracking without revealing original data.

---

## 4. Why would you choose Block strategy?

### Answer

When processing sensitive data is prohibited by compliance requirements.

---

## 5. Why does HITL require checkpointing?

### Answer

Because execution pauses and must later resume from the saved state.

---

## 6. What is the purpose of `before_agent()`?

### Answer

To validate inputs before any model reasoning or tool execution occurs.

---

## 7. What is the purpose of `after_agent()`?

### Answer

To validate outputs before they are returned to the user.

---

## 8. Why are input guardrails usually cheaper?

### Answer

Because blocked requests avoid expensive model calls.

---

## 9. What is defense-in-depth in Guardrails?

### Answer

Using multiple guardrail layers so failures in one layer are caught by others.

---

## 10. Which guardrail should execute first?

### Answer

Typically input filtering and authentication checks should execute first to prevent unnecessary processing.

---

## 11. What are common HITL use cases?

### Answer

Financial transactions, external emails, infrastructure changes, and destructive database operations.

---

## 12. Why are layered guardrails preferred in production?

### Answer

Because modern AI systems face multiple risks that cannot be fully mitigated by a single validation mechanism.

---

# Advanced Interview Questions

## Why should PII detection run both before and after the agent?

### Answer

Input scanning prevents sensitive data from entering the system, while output scanning prevents accidental leakage during generation.

---

## Why is deterministic filtering usually the first layer?

### Answer

Because it is fast, inexpensive, and eliminates obvious violations before invoking costly models.

---

## Why should Human-in-the-Loop be placed before tool execution?

### Answer

Because the risky action must be approved before it actually occurs.

---

## How would you design guardrails for a healthcare chatbot?

### Answer

Use:

* Input filtering
* PII detection
* Medical safety validation
* Output compliance checks
* Human escalation for high-risk cases

---

# Best Interview One-Liner

> "Production AI systems use layered guardrails combining deterministic filters, PII protection, human approval workflows, and model-based safety checks to ensure security, compliance, and reliability."
