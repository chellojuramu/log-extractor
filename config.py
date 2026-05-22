# config.py

# Input log file name/path
INPUT_LOG_FILE = "batch.log"

# Output file name
OUTPUT_FILE = "extracted_exceptions.txt"

# Maximum number of exception samples needed
MAX_SAMPLES = 5

# Main log line to identify the failed contact creation
START_LINE_KEYWORD = "Exception creating contact for eventId="

# Extra confirmation keyword in the same start line
START_LINE_END_KEYWORD = "Skipping event."

# Exception line matching details
EXCEPTION_KEYWORDS = [
    "HttpClientErrorException$Conflict",
    "409 Conflict",
    "https://api.hubapi.com/crm/v3/objects/contacts",
    "Contact already exists",
    "Existing ID:",
    "CONFLICT"
]

# Stack trace lines to include after the exception
STACK_TRACE_KEYWORDS = [
    "HubSpotBatch.createContact",
    "HubSpotBatch.processEvents",
    "BatchConfig.processHubSpotEvents"
]

# How many lines to check after the start line
LOOKAHEAD_LINES = 50