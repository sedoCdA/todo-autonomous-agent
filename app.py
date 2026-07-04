from planner import create_plan
from executor import execute_plan
from reflection import review
from document import generate_doc

@app.post("/agent")

def agent(req: Request):

    plan = create_plan(req.request)

    result = execute_plan(
        req.request,
        plan
    )

    review_result = review(result)

    path = generate_doc(result)

    return {

        "plan": plan,

        "review": review_result,

        "document": path

    }