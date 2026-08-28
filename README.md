# AI-CAD-Engineer

AI-powered engineering system that converts natural-language design requirements into engineering calculations and automatically generates 3D CAD models in CATIA V5.

## 🚀 Overview

AI-CAD-Engineer allows users to describe what they want to design using simple natural language.

For example:

> "I want a bracket that can hold 5 kg."

The system processes the requirement, extracts engineering parameters, performs preliminary engineering calculations, and sends the resulting design parameters to CATIA V5 to generate a 3D CAD model.

## ⚙️ Workflow

Natural Language Requirement
        ↓
AI Requirement Extraction
        ↓
Engineering Calculations
        ↓
Design Parameters
        ↓
CATIA V5 Automation
        ↓
3D CAD Model

## 🧠 Features

- Natural-language engineering requirements
- AI-based requirement extraction
- Preliminary engineering calculations
- Safety factor consideration
- Automatic geometry selection
- CATIA V5 automation using Python
- Automatic 3D CAD part generation
- Modular engineering architecture

## 🛠️ Technologies

- Python
- CATIA V5
- pywin32
- Python COM automation
- AI / LLM-based requirement parsing

## 📁 Project Structure

```text
AI-CAD-Engineer/
│
├── src/
│   ├── ai/
│   ├── catia/
│   ├── engineering/
│   ├── optimization/
│   └── simulation/
│
├── main.py
├── requirements.txt
├── .gitignore
└── Product1.CATProduct

Example
(Input)
I want a bracket that can hold 5 kg.

AI-generated requirements

{
  "component": "L-bracket",
  "load_kg": 5,
  "safety_factor": 2.0,
  "material": "Steel",
  "max_displacement_mm": 0.5
}

Preliminary design

Component: L-bracket
Load: 5 kg
Force: 49.05 N
Safety Factor: 2.0
Material: Steel

Width: 100 mm
Height: 60 mm
Base Depth: 40 mm
Selected Thickness: 3 mm

The resulting parameters are then used to generate the CAD model in CATIA V5.

#when run the code must open the catia v5 
