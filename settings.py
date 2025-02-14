
from pathlib import Path

subreddits = [
    "AmItheAsshole",
    "antiwork",
    "AskMen",
    "ChoosingBeggars",
    "hatemyjob",
    "NoStupidQuestions",
    "pettyrevenge",
    "Showerthoughts",
    "TooAfraidToAsk",
    "TwoXChromosomes",
    "unpopularopinion",
    "confessions",
    "confession"
    ]
    
subreddits_excluded = [
    "r/CFB",
]

banned_keywords =["porn", "sex", "jerking off"]

# choices "polly","balcon"
voice_engine = "polly" 

total_posts_to_process = 5
minimum_submission_score = 5000
title_length_minimum = 20
title_length_maximum = 100
maximum_length_self_text = 5000
minimum_num_comments = 200
submission_limit = 1000
number_of_thumbnails = 3
max_video_length = 600 # Seconds
comment_limit = 600

assets_directory = "assets"
temp_directory = "temp"
audio_directory = str(Path("temp"))
fonts_directory = str(Path(assets_directory,"fonts"))
image_backgrounds_directory = str(Path(assets_directory,"image_backgrounds"))
images_directory = str(Path(assets_directory,"images"))
thumbnails_directory = str(Path(assets_directory,"images"))
background_directory = str(Path(assets_directory,"backgrounds"))
video_overlay_filepath = str(Path(assets_directory,"particles.mp4"))
videos_directory = "videos"
background_opacity = 0.5
background_volume = 0.5


video_height = 720
video_width = 1280
clip_size = (video_width, video_height)

disablecompile = False
disableupload = True

enable_overlay = True

# Newcaster Settings
enable_newscaster = False
newscaster_remove_greenscreen = True
newscaster_greenscreen_color = [1, 255, 17] # Enter the Green Screen RGB Colour 
newscaster_greenscreen_remove_threshold = 100
newscaster_filepath = str(Path(assets_directory,"newscaster.mp4").resolve())
newscaster_position = ("left","bottom")
newcaster_size = (video_width * 0.5, video_height * 0.5)

pause = 1 # Pause after speech
soundeffects_directory = str(Path(assets_directory,"soundeffects"))

text_bg_color = "#1A1A1B"
text_bg_opacity = 1
text_color = "white"
text_font = "Verdana-Bold"
text_fontsize = 32

download_enabled = True