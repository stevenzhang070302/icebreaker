from typing import List, Dict, Any

from langchain.output_parsers import PydanticOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field


class Summary(BaseModel):
    bio: str = Field(description="A short bio about the person")
    interesting_facts: List[str] = Field(description="Two interesting facts about them")
    mbti: str = Field(description="MBTI personality type")
    net_worth: str = Field(description="Guestimate their Net worth")
    hobbies: str = Field(description="Hobbies")
    favorite_books: str = Field(description="Favorite books")
    favorite_movies_genres: str = Field(description="Favorite movies genres")
    favorite_music_genres: str = Field(description="Favorite music genres")
    favorite_food_example_dishes: str = Field(
        description="Favorite food example dishes"
    )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "bio": self.bio,
            "interesting_facts": self.interesting_facts,
            "mbti": self.mbti,
            "net_worth": self.net_worth,
            "hobbies": self.hobbies,
            "favorite_books": self.favorite_books,
            "favorite_movies_genres": self.favorite_movies_genres,
            "favorite_music_genres": self.favorite_music_genres,
            "favorite_food_example_dishes": self.favorite_food_example_dishes,
        }


summary_parser = PydanticOutputParser(pydantic_object=Summary)
