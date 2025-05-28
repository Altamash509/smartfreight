-- models/stg_shipments.sql

SELECT
    'SHP123' AS shipment_id,
    'FedEx' AS carrier,
    'US-Northeast' AS region,
    '2024-05-01'::DATE AS expected_delivery,
    '2024-05-03'::DATE AS actual_delivery,
    CASE
        WHEN DATEDIFF('day', '2024-05-01', '2024-05-03') > 0 THEN 'Late'
        ELSE 'On Time'
    END AS delivery_status
