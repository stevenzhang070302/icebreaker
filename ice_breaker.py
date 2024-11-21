import os
from dotenv import load_dotenv

from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI

from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from output_parser import summary_parser, Summary

load_dotenv()


def ice_break_with(name: str) -> tuple[Summary, str]:
    linkedin_username = linkedin_lookup_agent(name=(name + " Linkedin Profile"))
    linkedin_data = scrape_linkedin_profile(linkedin_username, mock=True)

    summary_template = """
        given the Linkedin information {information} about a person, I want you to create and speculate based on given information on the following:
        1. a short bio about the person
        2. two interesting facts about them
        3. MBTI personality type
        4. Guestimate their Net worth
        5. Hobbies
        6. Favorite books
        7. Favorite movies genres
        8. Favorite music genres
        9. Favorite food example dishes

        \n{format_instructions}
    """
    # Prompt template
    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
        partial_variables={
            "format_instructions": summary_parser.get_format_instructions()
        },
    )
    # partial variables are used when we have a static defined prompt template we know before we run it

    # Chat model
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo", max_tokens=600)

    # Chain
    chain = summary_prompt_template | llm | summary_parser

    res: Summary = chain.invoke(input={"information": linkedin_data})
    return res, linkedin_data.get("profile_pic_url")


if __name__ == "__main__":
    print("Ice Breaker Enter")
    print(ice_break_with("Steven Zhang Georgia Tech Startup Create-x Founder"))
    # ice_break_with("Yingtong Pan Wendy at Georgia Tech VIP")
