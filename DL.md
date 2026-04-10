# 🤖 Artificial Intelligence (AI) — Practical Overview

## 📌 What is AI?
Artificial Intelligence (AI) refers to systems that can perform tasks typically requiring human intelligence, such as:
- Understanding language
- Recognizing patterns
- Making decisions
- Learning from data

---

## 🧠 Core Types of AI

### 1. Narrow AI (Weak AI)
- Designed for specific tasks
- Examples: chatbots, recommendation systems, image recognition

### 2. General AI (AGI)
- Hypothetical systems with human-level intelligence across domains

### 3. Superintelligence
- AI that surpasses human intelligence (theoretical)

---

## ⚙️ Key Subfields

### 📊 Machine Learning (ML)
AI systems that learn from data instead of explicit programming.

```python id="ml-basic"
# Simple example: predicting y from x
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X, y)
prediction = model.predict([[5]])
