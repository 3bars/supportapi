# Copyright 2021 Amazon Inc.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

# sources:
# boto3 docs https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support.html
# support api referece https://docs.aws.amazon.com/awssupport/latest/APIReference/API_RefreshTrustedAdvisorCheck.html

#!/usr/bin/python3

import os
import boto3
from botocore.parsers import ResponseParser

boto3.setup_default_session(profile_name='work', region_name='us-east-1')
support_client = boto3.client('support')


# Discribe Current Case (in case the account isn't new)
response = support_client.describe_cases()

print(response)
# Create a case
