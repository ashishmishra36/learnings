🧠 Goal

You want a POC that:

Runs a job/process (could be a dummy script or data validation).

Detects a failure (non-zero exit, or data mismatch).

Sends a notification email automatically via AWS Lambda + SNS.

All of this will be under the Free Tier, and you’ll use open-source or built-in AWS components only.

⚙️ Architecture Overview

Flow:

A job (Python script / cron / Step Function / container) runs and reports success/failure to CloudWatch Logs or CloudWatch Metrics.

A CloudWatch Alarm is triggered when a “failure” metric is detected.

The Alarm invokes a Lambda function, which sends an alert via AWS SNS (email).

You’ll use:

✅ AWS Lambda (Free Tier)

✅ AWS CloudWatch (Free Tier)

✅ AWS SNS (Free Tier)

✅ Python (Open Source)

🧩 Step-by-Step Implementation
1. Create a Dummy Job

This can be a simple Python script that randomly fails — simulating your process.

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


You can run this locally or from an EC2 / Lambda job — each run pushes a metric.

2. Create a CloudWatch Alarm

Create an alarm that triggers when the job fails:

Go to CloudWatch → Alarms → Create Alarm

Metric namespace: JobMonitoring

Metric name: JobStatus

Threshold: Less than 1

Period: 1 minute or per run frequency

Action: Trigger a Lambda function

3. Create the Lambda Alert Function

Lambda will handle email notifications through SNS.

Example code (lambda_alert.py):

import boto3
import json
import os

sns = boto3.client('sns')

def lambda_handler(event, context):
    alarm_name = event['detail']['alarmName']
    reason = event['detail']['state']['reason']
    message = f"ALERT: {alarm_name}\nReason: {reason}"
    
    sns.publish(
        TopicArn=os.environ['SNS_TOPIC_ARN'],
        Subject='Job Failure Alert',
        Message=message
    )


Deploy this Lambda:

Runtime: Python 3.12

Add environment variable SNS_TOPIC_ARN

4. Create an SNS Topic for Email Alerts

Go to SNS → Topics → Create topic

Name: job-failure-alerts

Create a subscription with your email.

Confirm the subscription from your email.

Use the Topic ARN in your Lambda environment variable.

5. Connect Alarm → Lambda

In your CloudWatch Alarm, under Actions, choose Lambda function → select your function.

Now when your job fails (metric < 1), CloudWatch triggers the Lambda, which sends an SNS email