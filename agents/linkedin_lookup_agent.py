import os
from dotenv import load_dotenv

from tools.tools import get_profile_url_tavily

load_dotenv()
from langchain_openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from langchain_core.tools import (
    Tool,
)  # Interfaces that help LLM to interact with the outside world
from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)

from langchain import hub  # Import the hub to use pre-made prompts


def lookup(name: str) -> str:
    """
    Lookup the linkedin profile page url given the person's name and search keywords.
    """
    llm = ChatOpenAI(
        temperature=0,
        model="gpt-3.5-turbo",
    )

    template = """
        Given their exact name and exact search keywords, {name_of_person}, I want you to find me the link to this persons's LinkedIn profile page.
        Your answer should contain only the LinkedIn URL to the profile page.
    """

    prompt_template = PromptTemplate(
        input_variables=["name_of_person"], template=template
    )

    tools_for_agent = [
        Tool(  # Logicial entity that tells us what to run and when to run based on desciption
            name="Crawl Google for linkedin profile page",
            func=get_profile_url_tavily,
            description="useful for when you need to get the Linkedin page url",
        ),
    ]

    # React agent
    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(
        agent=agent, tools=tools_for_agent, verbose=True
    )  # Executes or orchestrates the agent

    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )

    linkedin_profile_url = result["output"]
    return linkedin_profile_url


if __name__ == "__main__":
    # linkedin_url = lookup(name = "Eden Marco Udemy Linkedin")
    linkedin_url = lookup(name="Steven Zhang Georgia Tech CREATE-X Startup Founder")
    # linkedin_url = lookup(name = "Yingtong Pan at Georgia Tech VIP Linkedin")
    print(linkedin_url)
