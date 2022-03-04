import pandas as pd
import sys
from pathlib import Path

pd.options.display.max_columns = None
summaries_clean_700_to_710_with_gpt = 'summaries_clean_700_to_710_with_gpt.pkl'
summaries_clean_700_to_710_with_gpt_clean = 'summaries_clean_700_to_710_with_gpt_clean.pkl'

def clean_gpt_summary(gpt_summary):
    gpt_summary = gpt_summary.replace('\n\n', '\n')
    gpt_summary = gpt_summary.strip()
    
    # remove leading and ending double quotes
    if gpt_summary[0] == '"':
        gpt_summary = gpt_summary[1:]
    if gpt_summary[-1] == '"':
        gpt_summary = gpt_summary[:-1]
    
    # remove unfinished last sentences
    if gpt_summary[-1] != '.':
        gpt_summary = gpt_summary[:gpt_summary.rindex('.')+1]
    
    return gpt_summary

if __name__ == "__main__":
    if Path(summaries_clean_700_to_710_with_gpt_clean).is_file():
        print(f"aborting because processed file {summaries_clean_700_to_710_with_gpt_clean} already exists")
        sys.exit(0)

    df = pd.read_pickle(summaries_clean_700_to_710_with_gpt)

    # manually exclude bad GPT summaries (empty values and gibberish)
    bad_pageid = [1354805, 3399000, 3649644, 4905815, 8075358,
                  8242641, 9251702, 10795788, 15139081, 17516530,
                  18908777, 26026669, 35932712, 37582573, 38640156,
                  38651052, 38763730, 45449571, 48254415, 50144579,
                  52628922, 55645310, 63897218, 67830517, 47711082]
    df = df[~df.pageid.isin(bad_pageid)]
    
    df['gpt_summary_clean'] = df.gpt_summary.apply(clean_gpt_summary)
    df.to_pickle(summaries_clean_700_to_710_with_gpt_clean)
