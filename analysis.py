import pandas as pd

def calculate_statistics(df):
    """Calculate basic statistics for student data."""
    stats = {
        'avg_quiz_score': df['quiz_scores'].mean(),
        'avg_completion_rate': df['completion_rate'].mean(),
        'avg_engagement_time': df['engagement_time'].mean()
    }
    return stats

def identify_engagement_trends(df):
    """Identify trends based on interaction counts and engagement time."""
    high_engagement = df[df['engagement_time'] > df['engagement_time'].mean()]
    return high_engagement

def score_vs_completion(df):
    """Correlate quiz scores with course completion rates."""
    correlation = df['quiz_scores'].corr(df['completion_rate'])
    return correlation

