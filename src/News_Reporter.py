from crewai import Agent, Task, Crew, Process
# from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain.tools import tool
# from langchain_community.document_loaders import WebBaseLoader
import os
from langchain_community.tools import DuckDuckGoSearchRun
from duckduckgo_search import DDGS
from datetime import datetime

# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

@tool("News Searching Tool")
def news_search_tool(query: str):
    """Search Internet for relevant information based on a query."""
    ddgs = DDGS()
    results = ddgs.text(keywords=query, region='wt-wt', safesearch='moderate', max_results=5)
    return results


class NewsAnalysisEngine:
    def __init__(self):
        # self.llm = ChatOpenAI(model="gpt-3.5-turbo", api_key=OPENAI_API_KEY)
        self.llm = ChatGroq(
            temperature=0,
            groq_api_key=GROQ_API_KEY,
            model_name="mixtral-8x7b-32768"
        )


    search_tool = DuckDuckGoSearchRun()

    def analyze_news(self, query: str) -> str:
        """Analyze news articles based on the given query."""
        # news_analysis_engine = self

        news_search_agent = Agent(
            role='News Searcher',
            goal='Generate key points for each news article from the latest news',
            backstory='Expert in analysing and generating key points from news content for quick updates.',
            tools=[news_search_tool, self.search_tool],
            allow_delegation=True,
            verbose=True,
            llm=self.llm,
            memory=True
        )

        writer_agent = Agent(
            role='Writer',
            goal='Identify all the topics received. Use the News search Tool to fetch the articles, then use the Search tool for detailed exploration of each topic. Summarise the retrieved information in depth for every topic.',
            backstory='Expert in crafting engaging narratives from complex information.',
            tools=[news_search_tool, self.search_tool],
            allow_delegation=True,
            verbose=True,
            llm=self.llm,
            memory=True
        )
        d = datetime.now().strftime("%Y-%m-%d")
        news_search_task = Task(
            description=f'Search for {query} related news and articles and create key description for each news.',
            agent=news_search_agent,
            tools=[self.search_tool,news_search_tool],
            expected_output=f"Key points and description and Long summary for each news article related to {query}"
        )
        
        writer_task = Task(
            description=f"""
            Go step by step:
            Step 1: Identify all the topics received and fetch news articles on todays Date :- {d}.
            Step 2: Use the Search tool to search for information on each topic one by one.
            Step 3: Go through every topic and write an in-depth long summary of the information retrieved no matter what it should be atleast 2000 words summary.
            Step 4: Your final Report Should be A detailed research Article or blog on the News.
            Final Step : You give A detailed and very long Report and make sure you give atleast 1-2 paragraphs of content on each topic you get 
            Don't skip any topic and Steps.
            """,
            agent=writer_agent,
            context=[news_search_task],
            tools=[self.search_tool,news_search_tool],
            expected_output="detailed and very very long Report and make sure you give atleast 1-2 paragraphs of content on each topic"
        )

        news_crew = Crew(
            agents=[news_search_agent, writer_agent],
            tasks=[news_search_task, writer_task],
            process=Process.sequential,
            manager_llm=self.llm
        )

        result = news_crew.kickoff()
        return result

# if __name__ == "__main__":
#     engine = NewsAnalysisEngine()
#     d = datetime.now().strftime("%Y-%m-%d")
#     result = engine.analyze_news(f"AI advancements Related news on {d}")
#     print(result)
