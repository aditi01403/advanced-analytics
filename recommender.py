
def recommend_funds(df, risk_preference):
    """Filters funds by risk grade and returns the top performers by Sharpe ratio"""
    filtered = df[df['Risk_Grade'].str.lower() == risk_preference.lower()]
    return filtered.sort_values(by='Sharpe_Ratio', ascending=False).head(3)
