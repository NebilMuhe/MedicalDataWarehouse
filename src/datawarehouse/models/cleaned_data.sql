{{ config(materialized='table') }}

WITH cleaned_data AS (
    SELECT
        "id",
        "message",
        "date",
        "media_path"
    FROM cleaned_data
)
SELECT * FROM cleaned_data