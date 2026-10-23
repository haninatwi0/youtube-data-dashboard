import plotly.express as px
import pandas as pd

def create_views_likes_scatter(df):
    fig = px.scatter(
        df, 
        x="views", 
        y="likes", 
        size="comment_count",      
        color="category_id",       
        hover_name="title",
        hover_data=["channel_title"],
        log_x=True, 
        log_y=True,
        title="YouTube Views vs. Likes (Bubble Size = Comments)"
    )
    fig.update_layout(template="plotly_white")
    return fig

def create_category_bar(df):
    category_stats = df.groupby('category_id')['views'].mean().reset_index()
    category_stats = category_stats.sort_values(by='views', ascending=False)

    fig = px.bar(
        category_stats,
        x='category_id',
        y='views',
        color='views',
        color_continuous_scale='Reds',
        title='Average Views per YouTube Category ID',
        labels={'category_id': 'Category ID', 'views': 'Avg Views'}
    )
    fig.update_layout(template="plotly_white")
    return fig

def create_engagement_box(df):
    df_copy = df.copy()
    df_copy['engagement_rate'] = ((df_copy['likes'] + df_copy['comment_count']) / df_copy['views']) * 100

    fig = px.box(
        df_copy, 
        x="category_id", 
        y="engagement_rate",
        color="category_id",
        title="Engagement Rate Distribution Across Categories (%)"
    )
    fig.update_layout(template="plotly_white")
    return fig

def create_time_series(df):
    df_copy = df.copy()
    df_copy['publish_time'] = pd.to_datetime(df_copy['publish_time'], errors='coerce')
    df_copy['publish_date'] = df_copy['publish_time'].dt.date
    daily_views = df_copy.groupby('publish_date')['views'].sum().reset_index()

    fig = px.line(
        daily_views, 
        x='publish_date', 
        y='views', 
        title='Total YouTube Views by Upload Date',
        labels={'publish_date': 'Date Published', 'views': 'Total Views'}
    )
    fig.update_xaxes(rangeslider_visible=True)
    fig.update_layout(template="plotly_white")
    return fig