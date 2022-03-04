import random
import pandas as pd
from string import Template

pd.options.display.max_columns = None
summaries_clean_700_to_710_with_gpt_clean = 'summaries_clean_700_to_710_with_gpt_clean.pkl'
quizdown = 'quizdown.md'

quizdown_settings = '''
---
shuffleQuestions: true
shuffleAnswers: false
nQuestions: 10
---
'''

quizdown_question_template = Template('''
# $title
Which version of the story was altered by a bot?
<br><br>
**First**
<br>
$first
<br><br>
**Second**
<br>
$second

1. [$first_checkbox] First
1. [$second_checkbox] Second

> $wikipedia_link
''')

def write_plot_to_file(row):
    gpt_is_first = random.choice([True, False])
    with open(quizdown, "a", encoding="utf-8") as f:
        print(quizdown_question_template.substitute(
            title = row.title.replace('_', ' '),
            first = row.gpt_summary_clean if gpt_is_first else row.summary_clean,
            second = row.summary_clean if gpt_is_first else row.gpt_summary_clean,
            first_checkbox = 'X' if gpt_is_first else ' ',
            second_checkbox = ' ' if gpt_is_first else 'X',
            wikipedia_link = f"https://en.wikipedia.org/wiki/{row.title}",
        ), file=f)

if __name__ == "__main__":    
    df = pd.read_pickle(summaries_clean_700_to_710_with_gpt_clean)

    # build and write quizdown
    with open(quizdown, "w") as f:
        print(quizdown_settings, file=f)
    
    df.apply(write_plot_to_file, axis=1)
