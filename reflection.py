from planner import client


def review(document):
    prompt = f"""
Review the document.

Check:
- Is it complete?
- Is every section present?
- Is formatting logical?
- Are assumptions reasonable?

If everything looks good, return only:

APPROVED

Otherwise explain what is missing.

Document:
{document}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content