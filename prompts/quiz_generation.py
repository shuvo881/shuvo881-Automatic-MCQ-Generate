from langchain.prompts import PromptTemplate




class Prompt:

    @staticmethod
    def generate():
        TEMPLATE="""
            Text:{text}
            You are an expert MCQ maker. Given the above text, it is your job to \
            create a quiz  of {number} multiple choice questions for {subject} students in {tone} tone. 
            Make sure the questions are not repeated and check all the questions to be conforming the text as well.
            Make sure to format your response like  RESPONSE_JSON below  and use it as a guide. \
            Ensure to make {number} MCQs.
            \nPlease respond in the following JSON format:\n
            {response_json}

            """
        
        return PromptTemplate(input_variables=["text", "number", "subject", "tone", "response_json"], template=TEMPLATE)
        
        