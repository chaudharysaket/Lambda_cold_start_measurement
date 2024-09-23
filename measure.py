import boto3
import time
import json

# Initialize boto3 clients
lambda_client = boto3.client('lambda')

# Variables
LAMBDA_FUNCTION_NAME = 'go-lambda'
COUNTER = 0
MAX_INVOCATIONS = 100

# Function to invoke Lambda
def invoke_lambda(function_name, counter):
    payload = json.dumps({'counter': counter})
    
    response = lambda_client.invoke(
        FunctionName=function_name,
        InvocationType='RequestResponse',  # Synchronous invocation
        Payload=payload
    )
    
    print(f"Lambda invoked with counter {counter}")
    
    return response['Payload'].read()

# Function to update Lambda environment variable
def update_lambda_env(function_name, counter):
    # Get the current Lambda configuration
    response = lambda_client.get_function_configuration(FunctionName=function_name)

    # Get existing environment variables
    env_variables = response['Environment']['Variables']
    
    # Update the NR_LAMBDA_COUNT environment variable
    env_variables['NR_LAMBDA_COUNT'] = str(counter)
    
    # Update the Lambda function's environment variables
    lambda_client.update_function_configuration(
        FunctionName=function_name,
        Environment={
            'Variables': env_variables
        }
    )
    
    print(f"NR_LAMBDA_COUNT updated to {counter}")

# Main process
while COUNTER < MAX_INVOCATIONS:
    # Invoke the Lambda function
    invoke_lambda(LAMBDA_FUNCTION_NAME, COUNTER)
    
    # Update the environment variable in the Lambda function
    update_lambda_env(LAMBDA_FUNCTION_NAME, COUNTER)
    
    # Increment the counter
    COUNTER += 1
    
    # Wait for 1 second before next iteration
    time.sleep(5)

print(f"Process completed. Lambda function invoked {MAX_INVOCATIONS} times.")
