!pip install datasets
!pip install scikit-learn
!pip install ibm-watson-machine-learning==1.0.312
import os, getpass
from pandas import read_csv
# [3] Watsonx API connection
# Enter the URL for Watson Machine Learning as per your WML Location
# Dallas : us-south
# Frankfurt : eu-de
# London : eu-gb
# Tokyo: jp-tok

credentials = {
    "url": "https://us-south.ml.cloud.ibm.com",
    "apikey": getpass.getpass("Please enter your WML api key (hit enter): ")
}
try:
    project_id = os.environ["PROJECT_ID"]
except KeyError:
    project_id = input("Please enter your project_id (hit enter): ")
project_id
import os, types
import pandas as pd
from ibm_boto3 import client
from botocore.client import Config
import ibm_boto3

def __iter__(self): return 0

# @hidden_cell
# The following code accesses a file in your IBM Cloud Object Storage. 
# It includes your credentials. 
# You might want to remove those credentials before you share the notebook.

cos_client = ibm_boto3.client(service_name='s3',
    ibm_api_key_id='ba8HGqqCQc6R2MJL0DMxsPYK1BEa59KKYQ9mKl2_HVcg',
    ibm_auth_endpoint="https://iam.cloud.ibm.com/oidc/token",
    config=Config(signature_version='oauth'),
    endpoint_url='https://s3.us-south.cloud-object-storage.appdomain.cloud'
)

bucket = 'bucket-srsueuz8tf1ur7p'
object_key = 'train_data (1).csv'
body = cos_client.get_object(Bucket=bucket, Key=object_key)['Body']

# Add missing iter method so pandas accepts body as file-like object
if not hasattr(body, "__iter__"): body.__iter__ = types.MethodType(__iter__, body)

train_data = pd.read_csv(body)
train_data.head(5)
import os, types
import pandas as pd
from botocore.client import Config
import ibm_boto3

def __iter__(self): return 0

# @hidden_cell
# The following code accesses a file in your IBM Cloud Object Storage. 
# It includes your credentials. 
# You might want to remove those credentials before you share the notebook.

cos_client = ibm_boto3.client(service_name='s3',
    ibm_api_key_id="ba8HGqqCQc6R2MJL0DMxsPYK1BEa59KKYQ9mKl2_HVcg",
    ibm_auth_endpoint="https://iam.cloud.ibm.com/oidc/token",
    config=Config(signature_version='oauth'),
    endpoint_url="https://s3.us-south.cloud-object-storage.appdomain.cloud"
)

bucket = 'bucket-srsueuz8tf1ur7p'
object_key = "test_data (1).csv"
body = cos_client.get_object(Bucket=bucket, Key=object_key)['Body']

# add missing iter method, so pandas accepts body as file-like object
if not hasattr(body, "__iter__"): body.__iter__ = types.MethodType(__iter__, body)

test_data = pd.read_csv(body)
test_data.head(5)
from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes
model_id = ModelTypes.FLAN_UL2
satisfaction_instruction = """

Classify whether the customer was satisfied or not based on the comment.

comment: The car was not cleaned properly and the service desk was slow.
satisfaction: 0

comment: The pickup was quick and smooth. Car was in great condition.
satisfaction: 1

comment: I waited over 30 minutes to get the car and the agent was rude.
satisfaction: 0

comment: Staff was helpful, and I had no issues with the rental process.
satisfaction: 1

comment:"""


from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams

parameters = {
    GenParams.MAX_NEW_TOKENS: 10
}
from ibm_watson_machine_learning.foundation_models import Model

model = Model(
    model_id=model_id,
    params=parameters,
    credentials=credentials,
    project_id=project_id
)
results = []
comments = list(test_data.Customer_Service)
satisfaction = list(test_data.Satisfaction.astype(str))

for input_text in comments:
    results.append(model.generate_text(prompt=" ".join([satisfaction_instruction, input_text])))
comments
satisfaction
results
business_area_instruction = """

Identify the business area based on the customer comment.
Choose from:
'Product: Functioning', 'Product: Pricing and Billing', 'Service: Accessibility',
'Service: Attitude', 'Service: Knowledge', 'Service: Orders/Contracts'.

comment: The staff was extremely rude and dismissive at the counter.
business area: 'Service: Attitude'

comment: I was charged extra despite returning the car on time.
business area: 'Product: Pricing and Billing'

comment: The car engine had issues and it broke down halfway through the trip.
business area: 'Product: Functioning'

comment: I couldn't access the booking website from my phone.
business area: 'Service: Accessibility'

comment:"""

from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams

parameters = {
    GenParams.MAX_NEW_TOKENS: 15
}
from ibm_watson_machine_learning.foundation_models import Model

model = Model(
    model_id=model_id,
    params=parameters,
    credentials=credentials,
    project_id=project_id
)
results = []
comments = list(test_data.Customer_Service)
area = list(test_data.Business_Area)

for input_text in comments:
    results.append(model.generate_text(prompt=" ".join([business_area_instruction, input_text])))
comments
area
results
