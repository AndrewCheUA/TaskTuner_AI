import os
from langchain.llms import OpenAI
from config import settings
from langchain import PromptTemplate


os.environ['OPENAI_API_KEY'] = settings.openai_api_key
llm = OpenAI(model_name='text-davinci-003',
             temperature=0.2,
             max_tokens=256)


def goals_proposition(list_of_goals):
    goals_proposition = """Instructions:
    Acting as a coach and productivity expert, evaluate and reformulate the user-provided goals to be clearer and more actionable.
    If a goal is already well-defined, keep it as is.
    
    
    Context:
    Name: [name]
    Preferred working/studying hours: [preferred_hours]
    Common challenges: [hold_back]
    Start of day preference: [start_preference]
    
    
    Query:
    {query}
    
    
    Output Indicator:
    Revised Goal 1: [Reformulated Goal 1 statement or original if already clear]
    Revised Goal 2: [Reformulated Goal 2 statement or original if already clear]
    Revised Goal 3: [Reformulated Goal 3 statement or original if already clear]
    
    Answer: """

    prompt_template = PromptTemplate(
        input_variables=["query"],
        template=goals_proposition
    )

    return llm(prompt_template.format(query=list_of_goals))