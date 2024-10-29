from crewai import Crew, Process
from tasks import research_task, write_task
from agents import news_researcher, news_writer

# Form the tech-focused crew with sequential process execution
crew = Crew(
    agents=[news_researcher, news_writer],
    tasks=[research_task, write_task],
    process=Process.sequential
)

# Execute tasks with input and print results
try:
    result = crew.kickoff(inputs={'topic': 'AI in healthcare'})

    # Verifying the result to ensure it's in the expected format
    if result:
        print("Task Execution Result:")
        print(result)
    else:
        print("No result returned. Please check task and agent configurations.")

except Exception as e:
    print("An error occurred during task execution:", e)
