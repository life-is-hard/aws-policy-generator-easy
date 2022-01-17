"""
Author: Manjur Khan
"""
""" Plan

service, action, resource
s3, read, arn:aws:s3:::YOUR-BUCKET
dynamodb, query, arn:aws:dynamodb:us-west-2:account-id:table/Books
"""

inputs = [
    "s3, read, arn:aws:s3:::YOUR-BUCKET",
    "dynamodb, query, arn:aws:dynamodb:us-west-2:account-id:table/Books",
    "dynamodb, put, arn:aws:dynamodb:us-west-2:account-id:table/Books",
]

statements = []  # this is all the statements

policy = {"Version": "2012-10-17", "Statement": statements}

mapping = {
    "s3": {
        "read": ["s3:GetObject*"],
        "list": ["s3:ListBucket"],
        "wrtie": ["s3:PutObject*"],
        "delete": ["s3:DeleteObject"],
    },
    "dynamodb": {
        "query": [
            "dynamodb:DescribeTable",
            "dynamodb:Query",
            "dynamodb:Scan"
        ],
        "read-only": [
            "dynamodb:GetItem",
            "dynamodb:BatchGetItem",
            "dynamodb:Scan",
            "dynamodb:Query",
            "dynamodb:ConditionCheckItem"
        ],
        "put": [
            "dynamodb:PutItem",
            "dynamodb:UpdateItem",
            "dynamodb:DeleteItem",
            "dynamodb:BatchWriteItem",
            "dynamodb:GetItem",
            "dynamodb:BatchGetItem",
            "dynamodb:Scan",
            "dynamodb:Query",
            "dynamodb:ConditionCheckItem"
        ],
        "delete": [
            "dynamodb:DeleteItem",
            "dynamodb:GetItem",
            "dynamodb:BatchGetItem",
            "dynamodb:Scan",
            "dynamodb:Query"
        ]
    }
}

for i in inputs:
    args = i.split(",")
    service = args[0].strip()
    action = args[1].strip()
    resources = args[2].strip()
    statement = {
        "Effect": "Allow",
        "Action": mapping[service][action],
        "Resource": resources
    }
    statements.append(statement)

import json

print(json.dumps(policy, indent=2, sort_keys=True))
