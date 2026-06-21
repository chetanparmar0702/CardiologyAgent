# Cardiology Agent

## Overview

The **Cardiology Agent** is an AI-powered healthcare assistant designed to provide personalized guidance related to heart health. The agent collects patient information, analyzes uploaded cardiac reports, and generates recommendations for managing cardiovascular conditions while following AI safety and ethical guidelines.

The solution leverages **Google Gemini 2.5 Flash** as the Large Language Model (LLM) to deliver intelligent, context-aware responses.

---

## Features

### Patient Information Collection

The agent gathers the following information:

* Patient Name
* Age
* Heart-related symptoms or concerns
* Medical history:

  * Diabetes
  * Hypertension (Blood Pressure)
  * High Cholesterol
  * Other relevant conditions
* Diet Preference:

  * Vegetarian
  * Non-Vegetarian
* Lifestyle Information:

  * Physical activity level
  * Work lifestyle

### Medical Report Analysis

The agent can analyze uploaded cardiac reports such as:

* Electrocardiogram (ECG/EKG)
* Cardiac Stress Test (Exercise Stress Test)
* Lipid Profile Reports
* Cholesterol Test Reports
* Other heart-related diagnostic reports

### Personalized Recommendations

Based on patient inputs and uploaded reports, the agent provides:

* Heart health insights
* Lifestyle improvement suggestions
* Diet recommendations
* Physical activity guidance
* Preventive care suggestions
* Recommendations regarding potential cardiac procedures (informational only)

### Responsible AI & Safety

The agent follows:

* AI Ethics Guidelines
* Medical Safety Guardrails
* Harm Avoidance Principles
* Respectful and Helpful Communication (HAM)

A medical disclaimer is always included in the generated response.

---

## System Prompt Behavior

The agent:

1. Greets the user.
2. Introduces itself as a Cardiology Agent.
3. Asks:

   > "How may I help you today?"
4. Collects required patient details.
5. Requests cardiac reports for analysis.
6. Reviews provided information.
7. Generates a personalized heart-health management plan.
8. Includes a medical disclaimer.

---

## Example Interaction

### User

Hello, how are you?

### Agent

Hello! Welcome to the Cardiology Agent.

I am your AI-powered cardiology assistant and I'm here to help you understand your heart health and provide general guidance based on your information and medical reports.

How may I help you today?

Please provide the following details:

* Name
* Age
* Heart-related symptoms or concerns
* Medical history (diabetes, hypertension, cholesterol, etc.)
* Diet preference (Veg/Non-Veg)
* Physical activity level

You may also upload your ECG, Stress Test, Lipid Profile, or other cardiac reports for a more personalized assessment.

---

## Technology Stack

| Component    | Technology                         |
| ------------ | ---------------------------------- |
| AI Model     | Gemini 2.5 Flash                   |
| Domain       | Healthcare / Cardiology            |
| Use Case     | Patient Guidance & Report Analysis |
| Safety Layer | AI Guardrails & Medical Disclaimer |

---

## Workflow

1. User initiates conversation.
2. Agent collects patient information.
3. User uploads cardiac reports.
4. Agent analyzes available data.
5. Agent generates personalized recommendations.
6. Agent displays medical disclaimer.

---

## Cost Estimation (Gemini 2.5 Flash)

### Pricing Assumptions

* Input Tokens: $0.30 per 1 Million Tokens
* Output Tokens: $2.50 per 1 Million Tokens
* Exchange Rate: 1 USD ≈ ₹83 INR

### Sample Usage

| Type   | Tokens | Cost (USD) | Cost (INR) |
| ------ | ------ | ---------- | ---------- |
| Input  | 65     | $0.0000195 | ₹0.0016    |
| Output | 1,365  | $0.0034125 | ₹0.2832    |
| Total  | 1,430  | $0.003432  | ₹0.2848    |

Approximate total cost per interaction: **₹0.28 INR**

---

## Medical Disclaimer

This application is intended for informational and educational purposes only and does not replace professional medical advice, diagnosis, or treatment. Users should always consult a qualified healthcare professional or cardiologist before making any medical decisions. In case of a medical emergency, seek immediate medical attention.
