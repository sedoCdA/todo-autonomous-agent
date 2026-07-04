from fastapi import FastAPI
from pydantic import BaseModel

from planner import create_plan
from executor import execute_plan
from reflection import review
from document import generate_doc

app = FastAPI()


class AgentRequest(BaseModel):
    request: str


@app.post("/agent")
def agent(req: AgentRequest):

    # Step 1: Create execution plan
    plan = create_plan(req.request)

    # Step 2: Execute the plan
    result = execute_plan(req.request, plan)

    # Step 3: Review the generated document
    review_result = review(result)

    # Step 4: Generate Word document
    path = generate_doc(result)

    return {
    "request": req.request,
    "plan": plan,
    "review": review_result,
    "document_path": path,
    "message": "Document generated successfully."
}
