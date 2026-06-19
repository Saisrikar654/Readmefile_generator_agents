import os
from fastapi import FastAPI
from pydantic import BaseModel
from crewai import Crew, Process

os.environ["CREWAI_TELEMETRY_OPT_OUT"] = "true"
os.environ["GEMINI_API_KEY"] =  "AIzaSyDv_BSSGX2S8ubdZQNT9ERUG3ZWeDaKges"

from agents.definitions import tech_writer,markdown_designer,portfolio_optimizer,qa_engineer
from agents.tasks import create_polish_task, created_draft_task,create_optimization_task,create_qa_task
 
app = FastAPI()

class ReadmeRequest(BaseModel):
    project_name: str 
    project_desc: str

@app.post("/generate")
async def generate_readme(data:ReadmeRequest):

    writer= tech_writer()
    desiginer=markdown_designer()
    optimizer = portfolio_optimizer()
    qa = qa_engineer()

    task1=created_draft_task(writer,data.project_name,data.project_desc)
    task2=create_polish_task(desiginer)
    task3 = create_optimization_task(optimizer)
    task4 = create_qa_task(qa)

    crew= Crew(
        agents=[writer,desiginer,optimizer, qa],
        tasks=[task1,task2,task3,task4],
        process=Process.sequential,
        verbose=False
    )

    result = await crew.kickoff_async()

    return {"markdown": str(result)} 
