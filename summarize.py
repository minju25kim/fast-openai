import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL")

client = OpenAI(api_key=OPENAI_API_KEY)

async def openai_summarize(link) -> dict:
    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[
            {
                "role": "system",
                "content": "You extract the link into JSON data.",
            },
            {
                "role": "user",
                "content": link,
            },
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "summary_schema",
                "schema": {
                    "type": "object",
                    "properties": {
                        "link": {
                            "description": "The link that appears in the input",
                            "type": "string",
                        },
                        "title": {
                            "description": "The title of the article",
                            "type": "string",
                        },
                        "date": {
                            "description": "The publication date of the article",
                            "type": "string",
                        },
                        "summary": {
                            "description": "A summary of the article content",
                            "type": "string",
                        },
                        "tags": {
                            "description": "Relevant tags or keywords for the article",
                            "type": "array",
                            "items": {
                                "type": "string"
                            }
                        }
                    },
                    "additionalProperties": False,
                },
            },
        },
    )

    return response.choices[0].message.content