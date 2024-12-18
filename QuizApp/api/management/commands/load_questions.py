from django.core.management.base import BaseCommand
from api.models import Question

class Command(BaseCommand):
    help = "Load default quiz questions"

    def handle(self, *args, **options):
        questions = [
    {"question_text": "What is the most important factor when scaling a web application?", 
     "option_a": "Database optimization", 
     "option_b": "Load balancing", 
     "option_c": "Caching", 
     "option_d": "Asynchronous processing", 
     "correct_answer": "Load balancing"},

    {"question_text": "Which design pattern would you use to implement a highly extensible plugin-based system?", 
     "option_a": "Singleton", 
     "option_b": "Observer", 
     "option_c": "Factory", 
     "option_d": "Strategy", 
     "correct_answer": "Factory"},

    {"question_text": "When should you use microservices architecture instead of monolithic architecture in a startup?", 
     "option_a": "When you're just starting out with a small team", 
     "option_b": "When scaling becomes important", 
     "option_c": "When the application is complex and requires rapid changes", 
     "option_d": "Both b and c", 
     "correct_answer": "Both b and c"},

    {"question_text": "Which of the following is the most critical consideration when implementing CI/CD pipelines?", 
     "option_a": "Automating deployment", 
     "option_b": "Automating testing", 
     "option_c": "Integration with version control", 
     "option_d": "Infrastructure as code", 
     "correct_answer": "Automating testing"},

    {"question_text": "What is the best way to ensure your product is meeting user needs in an early-stage startup?", 
     "option_a": "Focus on building features based on customer feedback", 
     "option_b": "Use market research data", 
     "option_c": "Release early and iterate frequently", 
     "option_d": "Develop a minimum viable product (MVP)", 
     "correct_answer": "Release early and iterate frequently"},

    {"question_text": "Which of these tools would you use to ensure your software is secure against common web vulnerabilities?", 
     "option_a": "SonarQube", 
     "option_b": "OWASP ZAP", 
     "option_c": "Jest", 
     "option_d": "Selenium", 
     "correct_answer": "OWASP ZAP"},

    {"question_text": "What’s the biggest advantage of adopting Agile methodologies in a startup environment?", 
     "option_a": "Faster product releases", 
     "option_b": "Flexibility to adapt to changes", 
     "option_c": "Better resource allocation", 
     "option_d": "Lower development cost", 
     "correct_answer": "Flexibility to adapt to changes"},

    {"question_text": "What would be your approach for handling technical debt in a fast-paced startup environment?", 
     "option_a": "Tackle it immediately by refactoring the codebase", 
     "option_b": "Defer addressing it until the product is stable", 
     "option_c": "Prioritize technical debt resolution based on user impact", 
     "option_d": "Completely rewrite the product every year", 
     "correct_answer": "Prioritize technical debt resolution based on user impact"},

    {"question_text": "Which method would you use to validate product-market fit in the early stages of a startup?", 
     "option_a": "Track customer retention and churn", 
     "option_b": "Survey customers about product satisfaction", 
     "option_c": "Measure customer engagement metrics", 
     "option_d": "All of the above", 
     "correct_answer": "All of the above"},

    {"question_text": "What is the key benefit of using containerization (e.g., Docker) in a startup's development and deployment process?", 
     "option_a": "Portability across different environments", 
     "option_b": "Improved performance", 
     "option_c": "Simplified team collaboration", 
     "option_d": "Reduced cloud infrastructure costs", 
     "correct_answer": "Portability across different environments"}
]
        for q in questions:
            Question.objects.create(**q)
        self.stdout.write(self.style.SUCCESS("Questions loaded successfully"))
