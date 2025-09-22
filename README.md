# Regex Pattern Matcher in Python
This Python script demonstrates how to use regular expressions 
(regex) to extract common data patterns from a block of sample text.



# Features

Extracts multiple data types using regex:

Email addresses
URLs
Phone numbers
Credit card numbers
Time formats (24-hour)
HTML tags
Hashtags
Currency amounts (USD format)
# Handles cases where:
>A pattern has no match
>None of the patterns match the sample text

Eg:
• Email address if not much with any gaven text:
>  - No match found for Email address
...

# How It Works:

> A dictionary of regex patterns is defined.
>The script uses re.findall() to search for each pattern in the provided sample text.
>The results are displayed in a structured  format.
