import re

# A sample block of text containing various types of information.
sample_text = """
Email address: firstname.lastname@company.co.uk
URL: https://subdomain.example.org/page
Phone number: 123.456.7890
Credit Card: 1234 5678 9012 3456
Time: 14:30
HTML: <img src="image.jpg" alt="description">
Hashtag: #example
Currency amounts: $19.99
"""

# Dictionary of patterns we want to detect in the text.
patterns = {
    "Email address": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",
    "URL": r"https?:\/\/(?:www\.)?[a-zA-Z0-9.-]+\.[a-z]{2,}(?:\/\S*)?",
    "Phone number": r"(?:\(\d{3}\)\s?|\d{3}[-.])\d{3}[-.]\d{4}",
    "Credit Card": r"(?:\d{4}[-\s]?){3}\d{4}",
    "Time": r"(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APMapm]{2})?",
    "HTML": r"<[^>]+>",
    "Hashtag": r"#\w+",
    "Currency amounts": r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?"
}

any_match_found = False
# Loop through each type of pattern and apply the regex to find matches in the sample text.
for label, regex in patterns.items():
    matches = re.findall(regex, sample_text)
    print(f"• {label}:")
# Print out the label along with any matches found.
    if matches:
        any_match_found = True  
        for match in matches:
            print(f"   - {match}")
    else:
        print(f"   - No match found for {label}")

if not any_match_found:
    print("\n- No match with any regex pattern.")






 
