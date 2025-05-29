-- models/stg_shipments.sql

SELECT
    shipment_id,
    carrier,
    region,
    expected_delivery,
    actual_delivery,
    CASE
        WHEN DATEDIFF('day', expected_delivery, actual_delivery) > 0 THEN 'Late'
        ELSE 'On Time'
    END AS delivery_status
FROM {{ source('raw', 'shipments') }}
