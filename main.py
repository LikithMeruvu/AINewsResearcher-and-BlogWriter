from src.News_Reporter import NewsAnalysisEngine
from src.Blog_Generator import BlogPostGenerator
from datetime import datetime


engine = NewsAnalysisEngine()
blog_post_generator = BlogPostGenerator()
d = datetime.now().strftime("%Y-%m-%d")
result = engine.analyze_news(f"Generative AI news and advancements today's Date is :-{d}")
print(result)

print("================================This is The Actual Blog post +++++++++++++++++++++++++")
blog_post = blog_post_generator.generate_blog_post(result)
print(blog_post)



