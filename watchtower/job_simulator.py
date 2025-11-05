# job_simulator.py
import random
import sys
import boto3

cloudwatch = boto3.client('cloudwatch', region_name='us-east-1')

job_name = "data_validation_job"
status = random.choice(["SUCCESS", "FAIL"])

print(f"Job Status: {status}")

metric_value = 1 if status == "SUCCESS" else 0

# Push metric to CloudWatch
cloudwatch.put_metric_data(
    Namespace='JobMonitoring',
    MetricData=[{
        'MetricName': 'JobStatus',
        'Dimensions': [{'Name': 'JobName', 'Value': job_name}],
        'Value': metric_value,
        'Unit': 'Count'
    }]
)

if status == "FAIL":
    sys.exit(1)
