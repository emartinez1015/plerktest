from drf_yasg import openapi

transaction_summary_list = dict(
    manual_parameters=[
        openapi.Parameter(
            "ini_date",
            in_=openapi.IN_QUERY,
            description="Initial Date",
            type=openapi.TYPE_STRING,
            required=True,
            example="2021-01"
        ),
        openapi.Parameter(
            "fin_date",
            in_=openapi.IN_QUERY,
            description="Final Date",
            type=openapi.TYPE_STRING,
            required=True,
        ),
    ]
)