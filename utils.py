import re

SQLI_PATTERNS = {
    r"(?i)(\bor\b\s+\d+=\d+)": "Classic bypass – makes SQL condition always true (e.g., OR 1=1)",
    r"(?i)union\s+select": "Combines results from two queries – may leak data",
    r"(?i)--": "SQL comment to cut off rest of statement – often used to skip checks",
    r"(?i)insert\s+into": "Used to insert rogue data",
    r"(?i)drop\s+table": "Can delete entire tables!",
    r"(?i)';": "Classic string break + inject attack",
    r"(?i)exec\s+xp_cmdshell": "Executes system commands – can lead to remote code execution",
    r"(?i)select\s+from\s+information_schema.tables": "Queries metadata about database tables",
    r"(?i)select\s+from\s+mysql.user": "Queries user privileges – may leak sensitive info",
    r"(?i)waitfor\s+delay": "Delays execution – can be used for timing attacks",
}

def detect_sqli(input_str):
    return [(pat, desc) for pat, desc in SQLI_PATTERNS.items() if re.search(pat, input_str)]
