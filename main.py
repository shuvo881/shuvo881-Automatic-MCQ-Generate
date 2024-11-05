from langchain.chains import LLMChain
from langchain.chains import SequentialChain
import pandas as pd
from langchain.callbacks import StdOutCallbackHandler
from LLM_model import gemini
from prompts import quiz_generation, evaluation_generation
import json
from config import RESPONSE_FORMATE




NUMBER=5 
SUBJECT="biology"
TONE="simple"
file_path=r"data/example.txt"

# Load Data
with open(file_path, 'r') as file:
    TEXT = file.read()
    
inp = {
    "text": TEXT,
    "number": NUMBER,
    "subject":SUBJECT,
    "tone": TONE,
    "response_json": json.dumps(RESPONSE_FORMATE, indent=2)
}
    
    
# Initialize the Gemini model with a callback handler
callback_handler = StdOutCallbackHandler()  # for logging to console


# creating chains

#for quiz:
quiz_prompt_template=quiz_generation.Prompt.generate()
eva_prompt_template=evaluation_generation.Prompt.generate()

quzi_generate_chain = LLMChain(llm=gemini.get(), prompt=quiz_prompt_template, output_key="quiz")
eval_generate_chain = LLMChain(llm=gemini.get(), prompt=eva_prompt_template, output_key="review")

# Main chain
quiz_gen_and_eval_chain = SequentialChain(chains=[quzi_generate_chain, eval_generate_chain],
                                               input_variables=["text", "number", "subject", "tone", "response_json"],
                                               output_variables=["quiz", "review"],
                                               callbacks=[callback_handler]
                                               )




response = quiz_gen_and_eval_chain(inp)


quiz = response.get('quiz')

#conver to json
try:
    # Attempt to parse the output as JSON
    quiz_json = json.loads(quiz)
except json.JSONDecodeError:
    raise("Error: The quiz output is not in valid JSON format.")
      

quiz_table_data = []
for key, value in quiz_json.items():
    mcq = value["mcq"]
    options = " | ".join(
        [
            f"{option}: {option_value}"
            for option, option_value in value["options"].items()
            ]
        )
    correct = value["correct"]
    quiz_table_data.append({"MCQ": mcq, "Choices": options, "Correct": correct})

quiz=pd.DataFrame(quiz_table_data)
quiz.to_csv("data/processed/quiz_ans.csv",index=False)

