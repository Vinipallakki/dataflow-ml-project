
# import apache_beam as beam
# from apache_beam.options.pipeline_options import PipelineOptions, StandardOptions, GoogleCloudOptions
# import json
# import time

# google_cloud_options.job_name = f"sensor-data-streaming-job-{int(time.time())}"

# class ParseMessage(beam.DoFn):
#     def process(self, element):
#         record = json.loads(element.decode('utf-8'))
#         yield record


# class CustomOptions(PipelineOptions):
#     @classmethod
#     def _add_argparse_args(cls, parser):
#         parser.add_argument('--input_topic')
#         parser.add_argument('--output_table')

# # Set pipeline options
# options = PipelineOptions()
# google_cloud_options = options.view_as(GoogleCloudOptions)
# google_cloud_options.project = 'nimble-courier-449405-f7'
# google_cloud_options.job_name = 'sensor-data-streaming-job'
# google_cloud_options.staging_location = 'gs://nimble-courier-449405-f7/staging'
# google_cloud_options.temp_location = 'gs://nimble-courier-449405-f7/temp'
# options.view_as(StandardOptions).runner = 'DataflowRunner'
# options.view_as(StandardOptions).streaming = True

# custom_options = options.view_as(CustomOptions)
# custom_options.input_topic = 'projects/nimble-courier-449405-f7/topics/sensor-data-topic'
# custom_options.output_table = 'nimble-courier-449405-f7:predictive_maintenance.raw_sensor_data'

# with beam.Pipeline(options=options) as p:
#     (p
#      | 'Read from Pub/Sub' >> beam.io.ReadFromPubSub(topic=custom_options.input_topic)
#      | 'Parse JSON' >> beam.ParDo(ParseMessage())
#      | 'Write to BigQuery' >> beam.io.WriteToBigQuery(
#             custom_options.output_table,
#             schema='timestamp:TIMESTAMP,machine_id:INTEGER,temperature:FLOAT,vibration:FLOAT,pressure:FLOAT',
#             write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND
#         ))

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions, StandardOptions, GoogleCloudOptions
import json
import time

class ParseMessage(beam.DoFn):
    def process(self, element):
        record = json.loads(element.decode('utf-8'))
        yield record

class CustomOptions(PipelineOptions):
    @classmethod
    def _add_argparse_args(cls, parser):
        parser.add_argument('--input_topic')
        parser.add_argument('--output_table')

# Set pipeline options
options = PipelineOptions()
google_cloud_options = options.view_as(GoogleCloudOptions)
google_cloud_options.project = 'nimble-courier-449405-f7'
google_cloud_options.job_name = f'sensor-data-streaming-job-{int(time.time())}'
google_cloud_options.staging_location = 'gs://nimble-courier-449405-f7/staging'
google_cloud_options.temp_location = 'gs://nimble-courier-449405-f7/temp'
options.view_as(StandardOptions).runner = 'DataflowRunner'
options.view_as(StandardOptions).streaming = True

custom_options = options.view_as(CustomOptions)
custom_options.input_topic = 'projects/nimble-courier-449405-f7/topics/sensor-data-topic'
custom_options.output_table = 'nimble-courier-449405-f7:predictive_maintenance.raw_sensor_data'

with beam.Pipeline(options=options) as p:
    (p
     | 'Read from Pub/Sub' >> beam.io.ReadFromPubSub(topic=custom_options.input_topic)
     | 'Parse JSON' >> beam.ParDo(ParseMessage())
     | 'Write to BigQuery' >> beam.io.WriteToBigQuery(
            custom_options.output_table,
            schema='timestamp:TIMESTAMP,machine_id:INTEGER,temperature:FLOAT,vibration:FLOAT,pressure:FLOAT',
            write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND
        ))



