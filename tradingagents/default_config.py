import os

DEFAULT_CONFIG = {
    "project_dir": os.path.abspath(os.path.join(os.path.dirname(__file__), ".")),
    "results_dir": os.getenv("TRADINGAGENTS_RESULTS_DIR", "./results"),
    "data_dir": "/Users/yluo/Documents/Code/ScAI/FR1-data",
    "data_cache_dir": os.path.join(
        os.path.abspath(os.path.join(os.path.dirname(__file__), ".")),
        "dataflows/data_cache",
    ),
    "user_portfolio_csv": os.getenv("TRADINGAGENTS_USER_PORTFOLIO", None),
    # LLM settings
    "llm_provider": "openai",
    "deep_think_llm": "o4-mini",
    "quick_think_llm": "gpt-4o-mini",
    "backend_url": "https://api.openai.com/v1",
    # Debate and discussion settings
    "max_debate_rounds": 1,
    "max_risk_discuss_rounds": 1,
    "max_recur_limit": 100,
    # Tool settings
    "online_tools": True,
    # Look-back windows tailored for long-term investing workflows
    "global_news_look_back_days": 120,
    "company_news_look_back_days": 180,
    "reddit_news_daily_limit": 20,
    "social_sentiment_look_back_days": 120,
    "technical_indicator_look_back_days": 365,
    "insider_activity_look_back_days": 365,
}
