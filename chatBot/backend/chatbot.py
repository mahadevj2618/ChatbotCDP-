import requests
from bs4 import BeautifulSoup

# CDP Documentation Links
docs_links = {
    "Segment": "https://segment.com/docs/",
    "mParticle": "https://docs.mparticle.com/",
    "Lytics": "https://docs.lytics.com/",
    "Zeotap": "https://docs.zeotap.com/home/en-us/"
}


def fetch_documentation(url):
    """Fetch and extract text from a documentation webpage."""
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            return "Error: Unable to access documentation."

        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')

        # Extracting useful text
        text = ' '.join([p.text for p in paragraphs if p.text])
        return text[:5000]  # Limit text to avoid overload
    except Exception as e:
        return str(e)


def get_relevant_info(platform, query):
    """Retrieve relevant steps to answer the 'how-to' question from documentation."""
    if platform not in docs_links:
        return "Platform not supported. Please choose from Segment, mParticle, Lytics, or Zeotap."

    documentation_text = fetch_documentation(docs_links[platform])

    # Simple keyword matching for quick response
    faq = {
        "Segment": {
            "new source": "To set up a new source in Segment, go to the Segment UI, click 'Sources', then click 'Add Source'. Select your source type and follow the setup instructions.",
            "tracking plan": "You can create a tracking plan in Segment by navigating to the 'Protocols' section and adding a new tracking plan."
        },
        "mParticle": {
            "user profile": "To create a user profile in mParticle, you need to send an Identify API request with the user attributes.",
            "events": "To track events in mParticle, integrate the SDK and use the logEvent method."
        },
        "Lytics": {
            "audience segment": "To build an audience segment in Lytics, navigate to the 'Audiences' tab, click 'New Segment', and use filters to define your audience."
        },
        "Zeotap": {
            "integrate data": "To integrate your data with Zeotap, follow the API documentation for batch and streaming data ingestion."
        }
    }

    # Check predefined answers first
    for keyword, answer in faq.get(platform, {}).items():
        if keyword in query.lower():
            return answer

    # If no predefined answer, return extracted documentation
    return f"Here’s what I found from the documentation: {documentation_text[:1000]}..."

