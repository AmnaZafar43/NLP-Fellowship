import re

def clean_transcript(transcript_list):
    # Join the list into a single string
    transcript = " ".join(transcript_list)
    # Remove timestamps using regex
    cleaned_transcript = re.sub(r'\d{1,2}:\d{2}', '', transcript)
    # Remove extra spaces and newlines
    cleaned_transcript = re.sub(r'\s+', ' ', cleaned_transcript).strip()
    return cleaned_transcript
