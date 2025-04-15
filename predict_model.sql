WITH input_data AS (
  SELECT
    ROW_NUMBER() OVER () AS row_id,
    timestamp,
    machine_id,
    temperature,
    vibration,
    pressure
  FROM
    `nimble-courier-449405-f7.predictive_maintenance.raw_sensor_data`
),
predictions AS (
  SELECT
    ROW_NUMBER() OVER () AS row_id,
    CENTROID_ID AS predicted_cluster_id
  FROM
    ML.PREDICT(
      MODEL `nimble-courier-449405-f7.predictive_maintenance.kmeans_model`,
      (
        SELECT
          temperature,
          vibration,
          pressure
        FROM `nimble-courier-449405-f7.predictive_maintenance.raw_sensor_data`
      )
    )
)
SELECT
  i.*,
  p.predicted_cluster_id
FROM
  input_data i
JOIN
  predictions p
ON
  i.row_id = p.row_id;
