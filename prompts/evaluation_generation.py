from langchain.prompts import PromptTemplate



class Prompt:

    @staticmethod
    def generate():
        TEMPLATE="""
            You are an expert english grammarian and writer. Given a Multiple Choice Quiz for {subject} students.\
            You need to evaluate the complexity of the question and give a complete analysis of the quiz. Only use at max 50 words for complexity analysis. 
            if the quiz is not at per with the cognitive and analytical abilities of the students,\
            update the quiz questions which needs to be changed and change the tone such that it perfectly fits the student abilities
            Quiz_MCQs:
            {quiz}

            Check from an expert English Writer of the above quiz:
            """
        return PromptTemplate(input_variables=["subject", "quiz"], template=TEMPLATE)