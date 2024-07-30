from datetime import datetime
from youtube_transcript_api import YouTubeTranscriptApi

from clean_text import clean_transcript
from save_to_file import save_to_txt

def get_youtube_transcript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    print(transcript)
    return "\n".join([entry['text'] for entry in transcript])

video_id = "5tvmMX8r_OM"
transcript = get_youtube_transcript(video_id)
print(transcript)
text=clean_transcript(transcript)
save_to_txt(text,file_name=f'video_output_{str(datetime.now().ctime()).replace(' ','').replace(':','')}')
