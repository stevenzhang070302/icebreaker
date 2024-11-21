import os
import requests
from dotenv import load_dotenv

load_dotenv()


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = True):
    """
    Scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn Profile
    """

    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/stevenzhang070302/c31d2ca8775b5d4e2d86c81c47c6dcad/raw/c0e8109e4cffca52b8a44a8b87c217370859dd75/steven-zhang.json"
        response = requests.get(
            linkedin_profile_url,
            timeout=10,
        )
    else:
        headers = {"Authorization": "Bearer " + os.environ["PROXYCURL_API_KEY"]}
        api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
        params = {
            "linkedin_profile_url": linkedin_profile_url,
            "extra": "include",
            "github_profile_id": "exclude",
            "facebook_profile_id": "exclude",
            "twitter_profile_id": "exclude",
            "personal_contact_number": "exclude",
            "personal_email": "exclude",
            "inferred_salary": "include",
            "skills": "include",
            "use_cache": "if-recent",
            "fallback_to_cache": "never",
        }
        response = requests.get(api_endpoint, params=params, headers=headers)
    data = response.json()
    # Reduce token size
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None) and k not in ["people_also_viewed"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data


if __name__ == "__main__":
    print(scrape_linkedin_profile("https://www.linkedin.com/in/stevenzhang070302/"))
