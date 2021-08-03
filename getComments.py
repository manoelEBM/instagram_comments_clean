from igramscraper.instagram import Instagram
import sys
import pandas as pd
from functions.export import export

post_code = sys.argv[1]
data_name = sys.argv[2]
num_comments = int(sys.argv[3])

df = pd.DataFrame()

comments_text = []

instagram = Instagram(sleep_between_requests=30)

comments = instagram.get_media_comments_by_code(post_code,num_comments)

for comment in comments['comments']:
    comments_text.append(comment.text)

df['comentários'] = comments_text

export(df, data_name)