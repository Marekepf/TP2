import os
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange, Dimension, Metric, RunReportRequest

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'datasourcetp2-xxxxxxxxx.json'

client = BetaAnalyticsDataClient()
property_id = "xxxxxxxxx"
starting_date = "8daysAgo"
ending_date = "yesterday"

request_api = RunReportRequest(
    property=f"properties/{property_id}",
    dimensions=[
        Dimension(name="landingPagePlusQueryString")
    ],
    metrics=[
        Metric(name="sessions")
    ],
    date_ranges=[DateRange(start_date=starting_date, end_date=ending_date)],
)

response = client.run_report(request_api)
print(response)
