# Customer Comment Classification using IBM Watsonx

This project demonstrates the application of IBM Watsonx Foundation Models to classify customer feedback data into two key categories:

1. *Customer Satisfaction* – Determines whether a customer was satisfied (1) or not (0) based on their written comment.
2. *Business Area Identification* – Classifies each comment into relevant business areas such as:
   - Service: Attitude
   - Product: Pricing and Billing
   - Service: Accessibility
   - Product: Functioning
   - etc.

## 🧠 Project Objective

The aim of this task is to leverage powerful pre-trained large language models (LLMs), specifically FLAN-UL2, for zero-shot classification of text data without requiring model retraining.

The model is deployed via IBM Watson Machine Learning (Watsonx) APIs, and the data is loaded securely from IBM Cloud Object Storage (COS).

## 🔍 Why This Matters

- *Real-time Analysis*: Helps businesses quickly identify customer pain points from feedback text.
- *No Training Needed*: Uses zero-shot inference, eliminating the need for labeled training data.
- *Seamless Cloud Integration*: Utilizes IBM Cloud for model access and storage, ensuring scalability and security.

## 📂 Dataset Description

The datasets consist of customer service-related comments with labeled columns:
- Customer_Service: The customer feedback text.
- Satisfaction: Binary label (1 or 0).
- Business_Area: Categorized business issue.

These are stored and accessed directly from IBM Cloud Object Storage for scalable data handling.

## ✅ Outcome

The project successfully integrates Watsonx FLAN-UL2 for:
- Predicting satisfaction directly from raw comments.
- Classifying comments into predefined business-related categories.

The results can be further used for:
- Customer satisfaction dashboards
- Operational issue tracking
- Service improvement decisions
