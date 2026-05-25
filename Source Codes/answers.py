import pandas as pd

nobel_dataframe = pd.read_csv('nobel.csv')

def answer_casing(question, answer):
    answer_template = f"""
    ==============================================================================================================
      {question}
    --------------------------------------------------------------------------------------------------------------
      {answer}
    ==============================================================================================================
    """
    print(answer_template)


question_2 = "Which decade had the highest ratio of US-born Nobel Prize winners to total winners in all categories?"
def highest_usa_winner_decade(df) -> int | None:
    df['decade'] = (df['year'] // 10) * 10
    total_decade = df.groupby('decade').size()
    usa_born = df[df['birth_country'] == 'United States of America']
    usa_decade = usa_born.groupby('decade').size()
    ratio = (usa_decade / total_decade)
    return ratio.idxmax()
max_decade_usa: int = highest_usa_winner_decade(nobel_dataframe)

# ANSWERS

answer_casing(question_2, max_decade_usa)
