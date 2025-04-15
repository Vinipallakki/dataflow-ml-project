CREATE OR REPLACE MODEL `nimble-courier-449405-f7.predictive_maintenance.kmeans_model`
OPTIONS(model_type='kmeans', num_clusters=3) AS
SELECT
  temperature,
  vibration,
  pressure
FROM
  `nimble-courier-449405-f7.predictive_maintenance.raw_sensor_data`;

