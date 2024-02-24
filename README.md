# surf-webpage-textual-content
analyzes the textual content of a webpage, identifying and ranking the most common words found within it

This Python script analyzes the textual content of a webpage, identifying and ranking the most common words found within it. The analysis excludes common English stopwords and additional specified non-informative words. Here's a brief overview:

Stopwords Preparation: It uses NLTK (Natural Language Toolkit) to download and set up a list of English stopwords. Additional non-informative words specific to the task are also defined and added to the stopwords list.

HTML Parsing: Implements a custom HTML parser, MyHTMLParser, extending HTMLParser from Python's standard library. This parser extracts and processes textual data from HTML, filtering out stopwords and non-alphabetic strings, and prepares a list of relevant words.

Fetching and Parsing Web Content: The fetch_and_parse function fetches HTML content from a specified URL, then uses MyHTMLParser to parse the content and extract a cleaned list of words.

Identifying Common Words: The get_most_common_words function analyzes the list of words from the parsed HTML content, using Python's Counter to identify and rank the most common words. It returns the specified number of the most frequent words along with their counts.

Main Execution: Demonstrates the script's functionality by analyzing the textual content of DePaul University's College of Computing and Digital Media (CDM) homepage. It prints the 25 most common words found on the page, excluding stopwords and other specified non-informative words.

This script is useful for web content analysis, SEO optimization, and understanding the focus of textual information on webpages. It showcases how to combine web scraping, natural language processing, and data filtering to extract meaningful insights from web content
