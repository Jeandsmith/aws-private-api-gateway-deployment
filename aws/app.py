#!/usr/bin/env python3
import os

import aws_cdk as cdk

from aws.aws_stack import AwsStack

app = cdk.App()

AwsStack(
    app,
    "private-api-stack",
    env=cdk.Environment(
        account=os.environ["CDK_DEFAULT_ACCOUNT"],
        region=os.environ["CDK_DEFAULT_REGION"],
    ),
)

app.synth()
