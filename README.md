# Automatic MCQ Generator

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-orange)

An Automatic Multiple-Choice Question (MCQ) Generator that creates quizzes and evaluations from input text using a language model. This tool is designed to assist educators, students, and content creators by generating customized quizzes based on specific subjects and tones.

---

## Table of Contents

- [Automatic MCQ Generator](#automatic-mcq-generator)
  - [Table of Contents](#table-of-contents)
  - [Project Overview](#project-overview)
  - [Features](#features)
  - [Architecture](#architecture)
  - [Setup and Installation](#setup-and-installation)
    - [Prerequisites](#prerequisites)
    - [Installation Steps](#installation-steps)
  - [Usage](#usage)
    - [Configuration Parameters](#configuration-parameters)
    - [Running the Script](#running-the-script)
  - [Example](#example)
  - [Output](#output)
  - [Dependencies](#dependencies)
  - [Contributing](#contributing)
  - [License](#license)
  - [Acknowledgments](#acknowledgments)

---

## Project Overview

The Automatic MCQ Generator utilizes advanced language models to generate multiple-choice questions from a given text input. It processes the text, generates questions, options, and correct answers, and provides an evaluation review. The final output is saved as a structured CSV file for easy access and integration into other systems.

## Features

- **Automatic Quiz Generation**: Generates MCQs based on input text, subject, and tone.
- **Evaluation Review**: Provides an evaluation of the generated quiz.
- **Customizable Parameters**: Allows customization of the number of questions, subject area, and tone.
- **Structured Output**: Outputs results in a CSV file for easy analysis and sharing.
- **Modular Design**: Easy to integrate with other systems or extend functionality.

## Architecture

The project is structured into several key components:

- **Data Input**: Reads and processes input text from a file.
- **Language Model Chains**: Uses `LLMChain` and `SequentialChain` from the `langchain` library to process data through the language model.
- **Prompt Templates**: Utilizes prompt templates for quiz generation and evaluation.
- **Data Output**: Parses the language model output and saves it as a CSV file.

## Setup and Installation

### Prerequisites

- Python 3.8 or higher
- Git (for cloning the repository)
- Access to the `gemini` language model (ensure credentials and API access)

### Installation Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/Automatic-MCQ-Generate.git
   cd Automatic-MCQ-Generate
