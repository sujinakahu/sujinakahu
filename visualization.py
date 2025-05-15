import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.analysis import calculate_statistics, identify_engagement_trends, score_vs_completion

def display_statistics(df):
    stats = calculate_statistics(df)
    st.subheader("Basic Statistics")
    for stat, value in stats.items():
        st.write(f"{stat.replace('_', ' ').title()}: {value:.2f}")

def plot_engagement_distribution(df):
    """Plot engagement time distribution."""
    st.subheader("Engagement Time Distribution")
    fig, ax = plt.subplots()
    sns.histplot(df['engagement_time'], kde=True, ax=ax)
    st.pyplot(fig)

def plot_score_vs_completion(df):
    """Scatter plot of quiz scores against completion rates."""
    st.subheader("Quiz Scores vs Completion Rates")
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x='quiz_scores', y='completion_rate', ax=ax)
    ax.set_xlabel("Quiz Scores")
    ax.set_ylabel("Completion Rate")
    st.pyplot(fig)
    
def run_dashboard(df):
    """Main function to run the Streamlit dashboard."""
    st.title("E-Learning Platform Analytics Dashboard")

    # Display statistics
    display_statistics(df)

    # Plot engagement distribution
    plot_engagement_distribution(df)

    # Plot score vs completion correlation
    plot_score_vs_completion(df)
    
    # Display correlation between scores and completion rate
    st.subheader("Score and Completion Correlation")
    correlation = score_vs_completion(df)
    st.write(f"Correlation between Quiz Scores and Completion Rate: {correlation:.2f}")

