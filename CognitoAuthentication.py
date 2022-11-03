### Setup
# Install pycognito: https://pypi.org/project/pycognito/
# Create user pool: https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-as-user-directory.html
# Create a user (account status must be 'CONFIRMED' before use): https://docs.aws.amazon.com/cognito/latest/developerguide/how-to-create-user-accounts.html
# Add an app client: https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-configuring-app-integration.html
# Integrate a REST API with an Amazon Cognito user pool: https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-enable-cognito-user-pool.html

### Imports
import os
import requests
from pycognito import Cognito

### Configuration
endpoint = "YOUR_ENDPOINT_HERE"
userPoolID = "YOUR_USER_POOL_ID__HERE"
appClintID = "YOUR_APP_CLIENT_ID_HERE"
cognitoUsername = "YOUR_COGNITO_USERNAME_HERE"
cognitoPassword = "YOUR_COGNITO_PASSWORD_HERE"
tokenFilePath = os.path.join(os.path.dirname(__file__), "token.txt")

### API call
def callAPI():
    # Global definitions
    global statusCode

    # Get token from token file or create token file if it doesn't exist
    tokenFile = open(tokenFilePath, "a+")
    tokenFile.seek(0)
    token = tokenFile.read()
    tokenFile.close()

    # Call API
    response = requests.get(endpoint, headers = {"Authorization" : token})
    statusCode = response.status_code

    # Call response
    print(response.text)

### Generate a new token if the saved token was invalid
def getToken():
    # Authenticate with Cognito
    user = Cognito(userPoolID, appClintID, username = cognitoUsername)
    user.authenticate(password = cognitoPassword)
    
    # Save the new ID token
    tokenFile = open(tokenFilePath, "w")
    tokenFile.write(user.id_token)
    tokenFile.close()

### Main
statusCode = 0
callAPI()
if statusCode != 200:
    getToken()
    callAPI()