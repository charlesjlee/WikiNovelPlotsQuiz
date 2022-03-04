# WikiNovelPlots Quiz
This repo takes ~200 stories from [WikiNovelPlots](https://github.com/charlesjlee/WikiNovelPlots), alters them using GPT-3, and then presents them as a quiz in a Hugo site using [quizdown](https://github.com/bonartm/hugo-quiz).

## Repro steps inside /scripts
input|step|output
--|--|--
[WikiNovelPlots](https://github.com/charlesjlee/WikiNovelPlots)| N/A, the novel summaries were already copied to this repo|`summaries_clean.pkl`
`summaries_clean.pkl`|`get_gpt_summaries.py`|`summaries_clean_700_to_710_with_gpt.pkl`
`summaries_clean_700_to_710_with_gpt.pkl`|`clean_gpt_summaries.py`|`summaries_clean_700_to_710_with_gpt_clean.pkl`
`summaries_clean_700_to_710_with_gpt_clean.pkl`|`generate_quiz.py`|`quizdown.md`

## GPT-3 details
The code (see `/scripts/get_gpt_summaries.py`) below was used to alter each summary. I made 233 requests and it cost me $4.29.
```python
PROMPT = 'Summarize and expand the following story to make it original, surreal, and magical:\n\n'

def get_gpt_summary(summary_clean):
    response = openai.Completion.create(
        engine="text-davinci-001",
        prompt=f"{PROMPT}{summary_clean}",
        temperature=1,
        max_tokens=300,
        top_p=0.5,
        frequency_penalty=1,
        presence_penalty=1
    )
    return response.get('choices')[0]['text']
```
