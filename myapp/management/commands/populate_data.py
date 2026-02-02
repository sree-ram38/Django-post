from typing import Any
from myapp.models import posts, Category
from django.core.management.base import BaseCommand
import random




class Command(BaseCommand):
    help = "this command insert post data"

    def handle(self, *args: Any, **options: Any):
        # deleting existing data
        posts.objects.all().delete()

        titles = [
        "The Future of AI",
        "Climate Change Solutions",
        "Remote Work Trends",
        "Quantum Computing Explained",
        "Renewable Energy Innovations",
        "Deep Learning Demystified",
        "Post-Pandemic Economic Outlook",
        "Blockchain in Finance",
        "Storytelling in Marketing",
        "Medical Technology Advances",
        "Space Exploration Challenges",
        "Psychology of Decision Making",
        "Evolution of Social Media",
        "The Art of Cooking",
        "Cultural Diversity in Society",
        "Sustainable Development Investments",
        "Globalization Impact",
        "Power of Mindfulness",
        "Online Learning Revolution",
        "Art and Technology Fusion",
        ]

        content = [
            "Exploring the future of artificial intelligence and its impact on society, including how AI is reshaping industries, influencing decision-making, transforming human interaction, and raising ethical questions about privacy, employment, and responsible innovation in a rapidly evolving digital world.",
            "Discovering solutions to combat climate change and protect the environment by examining sustainable practices, renewable resources, policy reforms, and global cooperation aimed at reducing carbon emissions and preserving ecosystems for future generations.",
            "Analyzing trends and challenges in remote work environments, focusing on productivity, work-life balance, digital collaboration tools, organizational culture, and the long-term implications of distributed teams on modern workplaces.",
            "An introduction to the principles and applications of quantum computing, explaining how quantum mechanics enables unprecedented computational power and how this technology could revolutionize fields such as cryptography, medicine, and complex problem-solving.",
            "Investigating the latest innovations in renewable energy sources, highlighting advancements in solar, wind, hydro, and bioenergy technologies that aim to create cleaner, more efficient, and sustainable power systems worldwide.",
            "Understanding the fundamentals of deep learning and neural networks by exploring how machines learn from data, recognize patterns, and drive breakthroughs in areas like computer vision, natural language processing, and artificial intelligence research.",
            "Examining the economic landscape in the aftermath of the COVID-19 pandemic, assessing recovery strategies, shifts in global markets, workforce changes, and the long-term financial impact on businesses and governments.",
            "Exploring the potential of blockchain technology in the financial sector, including its role in enhancing transparency, security, decentralization, and efficiency in transactions, payments, and digital asset management.",
            "Harnessing the power of storytelling to create compelling marketing campaigns that connect emotionally with audiences, strengthen brand identity, and influence consumer behavior through authentic and engaging narratives.",
            "Highlighting breakthroughs and advancements in medical technology, showcasing innovations that improve diagnosis, treatment, patient care, and overall healthcare outcomes through cutting-edge research and digital transformation.",
            "Addressing the obstacles and opportunities in space exploration by examining technological challenges, international collaboration, scientific discovery, and humanity's pursuit of understanding the universe beyond Earth.",
            "Exploring the psychological factors influencing decision-making processes, including cognitive biases, emotional responses, social influences, and mental frameworks that shape human behavior in personal and professional contexts.",
            "Tracing the evolution of social media platforms and their impact on society, analyzing how digital communication has transformed relationships, information sharing, culture, and public discourse across the globe.",
            "Celebrating the art of cooking and culinary creativity by exploring diverse cuisines, innovative techniques, cultural traditions, and the joy of transforming ingredients into meaningful and expressive dishes.",
            "Promoting inclusivity and embracing diversity in modern communities by encouraging equal opportunities, mutual respect, cultural understanding, and social harmony in an increasingly interconnected world.",
            "Investigating sustainable development initiatives and their impact on the future, focusing on balancing economic growth, environmental protection, and social well-being to achieve long-term global sustainability.",
            "Examining the effects of globalization on local and global economies, discussing trade, cultural exchange, economic interdependence, and the challenges faced by nations in a highly connected marketplace.",
            "Embracing mindfulness practices for enhanced well-being and productivity by incorporating techniques that improve focus, reduce stress, foster emotional resilience, and support a balanced lifestyle.",
            "Revolutionizing education through online learning platforms and resources, highlighting how digital education expands access, personalizes learning experiences, and reshapes traditional teaching models.",
            "Exploring the intersection of art, design, and technology in the digital age, showcasing how creative expression and innovation merge to shape modern aesthetics, user experiences, and cultural trends.",
        ]

        img_url = [
            'https://picsum.photos/id/1/200/300',
            'https://picsum.photos/id/2/200/300',
            'https://picsum.photos/id/3/200/300',
            'https://picsum.photos/id/4/200/300',
            'https://picsum.photos/id/5/200/300',
            'https://picsum.photos/id/6/200/300',
            'https://picsum.photos/id/7/200/300',
            'https://picsum.photos/id/8/200/300',
            'https://picsum.photos/id/9/200/300',
            'https://picsum.photos/id/10/200/300',
            'https://picsum.photos/id/11/200/300',
            'https://picsum.photos/id/12/200/300',
            'https://picsum.photos/id/13/200/300',
            'https://picsum.photos/id/14/200/300',
            'https://picsum.photos/id/15/200/300',
            'https://picsum.photos/id/16/200/300',
            'https://picsum.photos/id/17/200/300',
            'https://picsum.photos/id/18/200/300',
            'https://picsum.photos/id/19/200/300',
            'https://picsum.photos/id/20/200/300',
        ]
        

        Catgories = Category.objects.all()
        for title, content_item, img_item in zip(titles, content, img_url):
            category = random.choice(Catgories)
            posts.objects.create(title=title, content=content_item, img_url=img_item, category=category)

        self.stdout.write(self.style.SUCCESS("Successfully inserted post data")) 