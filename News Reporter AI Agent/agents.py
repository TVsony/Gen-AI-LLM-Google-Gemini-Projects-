from crewai import Agent
from tools import tool
from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()

# Initialize Google Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    verbose=True,
    temperature=0.5,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Define topic dynamically for both agents
topic = "AI and technology advancements"

# Creating a senior researcher agent with memory and verbose mode
try:
    news_researcher = Agent(
        role="Senior Researcher",
        goal=f"Uncover groundbreaking technologies in {topic}",
        verbose=True,
        memory=True,
        backstory=(
            "Driven by curiosity, you're at the forefront of innovation, "
            "eager to explore and share knowledge that could change the world."
        ),
        tools=[tool],
        llm=llm,
        allow_delegation=True
    )

    # Creating a writer agent responsible for writing tech news blogs
    news_writer = Agent(
        role="Writer",
        goal=f"Narrate compelling tech stories about {topic}",
        verbose=True,
        memory=True,
        backstory=(
            "With a flair for simplifying complex topics, you craft engaging "
            "narratives that captivate and educate, bringing new discoveries "
            "to light in an accessible manner."
        ),
        tools=[tool],
        llm=llm,
        allow_delegation=False
    )

    print("Agents initialized successfully.")

except Exception as e:
    print("An error occurred during agent setup:", e)

