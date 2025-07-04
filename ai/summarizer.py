import os

import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_job(job_description: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Summarize this job clearly."},
            {"role": "user", "content": job_description}
        ]
    )
    return response['choices'][0]['message']['content']
