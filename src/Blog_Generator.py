import os
import google.generativeai as genai
from dotenv import load_dotenv

class BlogPostGenerator:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("GOOGLE_API_KEY")
        self.model = genai.GenerativeModel('gemini-1.5-pro-latest')

    def generate_blog_post(self, research_data):
        prompt = self.create_prompt(research_data)
        response = self.model.generate_content(prompt)
        return response.text

    def create_prompt(self, research_data):
        prompt = f"""
        Write a comprehensive 4000-5000 word blog post covering the following topics:
        {research_data}
        The blog post should be well-structured with the following elements:
        - Clear and informative introduction that provides an overview of the key topics
        - Detailed sections with subheadings for each major topic
        - Bullet point lists to highlight key facts, statistics, and insights
        - Smooth transitions between sections to guide the reader
        - In-depth analysis and commentary on the implications and significance of the topics
        - Comparisons to industry trends and competitors where relevant
        - Forward-looking predictions and speculations on the future developments
        - Conclusion that summarizes the main takeaways and leaves the reader with a strong impression
        Use a conversational yet authoritative tone throughout the blog post. Avoid jargon and explain technical concepts in simple terms. Incorporate relevant data points, expert quotes, and real-world examples to support the analysis. The writing should be concise, engaging, and informative, avoiding unnecessary fluff or filler content. Maintain a brisk pace and focus on delivering valuable insights to the reader. The final output should be between 4000-5000 words, with a well-structured flow that keeps the reader interested and informed from start to finish.
        """
        return prompt

# if __name__ == "__main__":
#     blog_post_generator = BlogPostGenerator()
#     research_data = "This is the research data that will be used to generate the blog post."
#     blog_post = blog_post_generator.generate_blog_post(research_data)
#     print(blog_post)