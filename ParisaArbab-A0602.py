"""
Author: Parisa Arbab
Date: Feb 19 2024
Statement:“I have not given or received any unauthorized assistance on this assignment.”
YouTube Link:https://youtu.be/hEaMGngBOZg

answered this question in the above link:
1.Show how you extended HTMLParser.
2. Show which methods you overwrote. __init__ and handle_data
3. Show how you restricted your search to webpages at CDM.

"""

from html.parser import HTMLParser
import re

from urllib.request import Request, urlopen
from collections import Counter

import nltk
from nltk.corpus import stopwords

# Download the stop words the first time
nltk.download('stopwords')
# Load the stop words in English
stop_words = set(stopwords.words('english'))
# Additional stop words
additional_stop_words = { 'u00253dtag0', 'u00253d', 'rev', 'u002f15', 'u002f_layouts', 'sp',  'js',  'ui', 'var'}
stop_words.update(additional_stop_words)



class MyHTMLParser ( HTMLParser ) :   #answer to Q1: extend HTMLParser
    """
    A custom HTML parser that extends the HTMLParser class to extract textual data from HTML.

    Methods overridden:
    - __init__: Initializes the parser and a list to store text.
    - handle_data: Processes and stores textual data found within HTML tags.
    """
    #Answer to Q2
    def __init__(self) :
        """Initialize the parser and a list to store extracted text."""
        super ().__init__ ()
        self.text = [ ]

    def handle_data(self, data) :
        """
        Overridden method to process textual data found within HTML tags.
        Uses regular expressions to find words, converting them to lowercase to ensure consistent counting.
        """
        words = re.findall ( r'\w+', data.lower () )
        filtered_words = [ word for word in words if word not in stop_words and len ( word ) > 1 and not word.isdigit () ]
        self.text.extend ( filtered_words )


def fetch_and_parse(url) :
    """
    Fetches HTML content from a given URL and uses MyHTMLParser to parse and extract words.

    Args:
        url (str): The URL to fetch and parse HTML content from.

    Returns:
        list: A list of words extracted from the HTML content.
    """
    headers = {'User-Agent' : 'Mozilla/5.0'}
    request = Request ( url, headers=headers )
    parser = MyHTMLParser ()
    with urlopen ( request ) as response :
        html = response.read ().decode ( 'utf-8' )
        parser.feed ( html )
    return parser.text


def get_most_common_words(url, limit=25) :
    """
    Identifies the most common words in the HTML content of a given URL.

    Args:
        url (str): The URL whose HTML content is to be analyzed.
        limit (int): The number of most common words to return.

    Returns:
        list: A list of tuples with the most common words and their counts.
    """
    words = fetch_and_parse ( url )  # Fetch and parse the HTML content to get words.
    counter = Counter ( words )  # Use Counter to count the occurrence of each word.
    return counter.most_common ( limit )  # Return the 'limit' most common words.


# Main execution
if __name__ == "__main__" :
    url = 'https://www.cdm.depaul.edu/'  # The URL to analyze (Q3:Restricting search to CDM webpages implicitly).
    most_common_words = get_most_common_words ( url )
    for i, (word, count) in enumerate ( most_common_words, start=1 ) :
        print ( f'{i}. {word}: {count}' )  # Print the 25 most common words with numbering.

# Answers to the questions:
# 1. Extending HTMLParser: Demonstrated by the MyHTMLParser class definition.
# 2. Methods Overwritten: __init__ and handle_data methods in MyHTMLParser class.
# 3. Restricting search to webpages at CDM: By directly using the CDM URL in the `get_most_common_words` function call.
