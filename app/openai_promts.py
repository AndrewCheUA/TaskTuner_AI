import os
from langchain.llms import OpenAI
from config import settings
from langchain import PromptTemplate


os.environ['OPENAI_API_KEY'] = settings.openai_api_key
llm = OpenAI(model_name='text-davinci-003',
             temperature=0.2,
             max_tokens=256)


def goals_proposition(list_of_goals, name, preferred_hours, hold_back, start_preference):
    goals_proposition = """Instructions:
    Acting as a coach and productivity expert, evaluate and reformulate the user-provided goals to be clearer and more actionable.
    If a goal is already well-defined, keep it as is.
    
    
    Context:
    Name: {name}
    Preferred working/studying hours: {preferred_hours}
    Common challenges: {hold_back}
    Start of day preference: {start_preference}
    
    
    User-provided goals:
    {list_of_goals}
    
    
    Output Indicator:
    Goal id: ; Goal Title: ; Goal Description: .
    
    
    Answer: """

    prompt_template = PromptTemplate(
        input_variables=["list_of_goals", "name", "preferred_hours", "hold_back", "start_preference"],
        template=goals_proposition
    )

    return llm(prompt_template.format(list_of_goals=list_of_goals, name=name, preferred_hours=preferred_hours,
                                      hold_back=hold_back, start_preference=start_preference))