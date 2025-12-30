# Imports from other modules
# from risk_scoring.recommendation import (
#     add_risk_recommendation,
#     ...
# )
# from config import OUTPUT_DF_FULL_DETAILED_FILE_PATH, DASHBOARD_OUTPUT_FILE_PATH

def stage4(earnings_df):
    """
    Stage 4 – Outputs, Recommendations & Alerting

    In the private version this stage generates the final output
    DataFrame that powers the dashboard and reporting layer.

    It includes:

      Pre-Earnings Insights
        - Risk-aware recommendations derived from the risk score
        - Natural-language style explanations for each recommendation
        - A pre-earnings risk flag based on recent behaviour and signals
        - Sector / sub-sector level risk indicators

      Post-Earnings Insights
        - Alerts for excessive price moves around earnings
        - Alerts where there is a large earnings surprise but muted / no
          corresponding price reaction
        - Alerts where the implied vs actual reaction diverge
        - Muted response alerts for beats / misses
        - Extreme volatility alerts relative to history

      Dashboard Output Preparation
        - Cleans and reshapes the detailed output into a compact
          dashboard-ready DataFrame (tickers, dates, scores, signals,
          alerts, summaries, etc.)
        - Writes a detailed CSV export for auditing / validation and a
          dashboard CSV for visualization.

    The full implementation is intentionally omitted in the public
    repository to protect proprietary recommendation and alert logic.
    """
    raise NotImplementedError(
        "Stage 4 implementation is omitted in the public version of this project."
    )
