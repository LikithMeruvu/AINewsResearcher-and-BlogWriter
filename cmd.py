import sys
from src.News_Reporter import NewsAnalysisEngine
from src.Blog_Generator import BlogPostGenerator
from datetime import datetime

def generate_news_and_blog(topic):
    """
    Generates news analysis and blog post for the given topic.

    Args:
        topic (str): The topic for which the news analysis and blog post should be generated.

    Returns:
        str: The news analysis result.
        str: The generated blog post.
    """
    engine = NewsAnalysisEngine()
    blog_post_generator = BlogPostGenerator()
    d = datetime.now().strftime("%Y-%m-%d")
    result = engine.analyze_news(f"{topic} today's Date is :-{d}")
    blog_post = blog_post_generator.generate_blog_post(result)
    return result, blog_post

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a topic as a command-line argument.")
        sys.exit(1)
    topic = " ".join(sys.argv[1:])
    news_analysis, blog_post = generate_news_and_blog(topic)
    print("================================News Analysis+++++++++++++++++++++++++")
    print(news_analysis)
    print("================================This is The Actual Blog post +++++++++++++++++++++++++")
    print(blog_post)