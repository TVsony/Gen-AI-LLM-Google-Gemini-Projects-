from crewai import Task
from tools import tool
from agents import news_researcher, news_writer

# Define topic for dynamic task description
topic = "AI"

# Research task
research_task = Task(
    description=(
        f"Identify the next big trend in {topic}. "
        "Focus on identifying pros and cons and the overall narrative. "
        "Your final report should clearly articulate the key points, "
        "its market opportunities, and potential risks."
    ),
    expected_output="A comprehensive 3-paragraph report on the latest AI trends.",
    tools=[tool],
    agent=news_researcher,
)

# Writing task with language model configuration
write_task = Task(
    description=(
        f"Compose an insightful article on {topic}. "
        "Focus on the latest trends and how it's impacting the industry. "
        "This article should be easy to understand, engaging, and positive."
    ),
    expected_output=f"A 4-paragraph article on {topic} advancements formatted as markdown.",
    tools=[tool],
    agent=news_writer,
    async_execution=False,
    output_file="new-blog-post.md"  # Specify output file name
)

# Running tasks (example)
try:
    research_result = research_task.run()
    print("Research Result:", research_result)
    
    write_result = write_task.run()
    print("Write Result:", write_result)
    
except Exception as e:
    print("An error occurred:", e)