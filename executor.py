from planner import client

def execute_plan(user_request, plan):

    prompt = f"""

User Request

{user_request}

Execution Plan

{plan}

Now execute every task and generate the complete business document.

"""

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    return response.choices[0].message.content