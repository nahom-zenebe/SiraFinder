# ai/resume_reviewer.py
def review_resume(resume_text: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Review this resume and give feedback."},
            {"role": "user", "content": resume_text}
        ]
    )
    return response['choices'][0]['message']['content']
