# CognitoAuthentication
This code snippet makes use of [AWS's Cognito service](https://aws.amazon.com/cognito/) to authenticate API requests. It is configured to store an ID token and is replaced when it expires so that your application can make minimal calls to Cognito to lower [costs (Cognito)](https://aws.amazon.com/cognito/pricing/). You will come accross the token expiry settings when setting up Cognito within the AWS console:
- [Create user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-as-user-directory.html)
- [Create a user (account status must be 'CONFIRMED' before use)](https://docs.aws.amazon.com/cognito/latest/developerguide/how-to-create-user-accounts.html)
- [Add an app client](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-configuring-app-integration.html)
- [Integrate a REST API with an Amazon Cognito user pool](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-enable-cognito-user-pool.html)

### Notes
- Both authorised and unauthorised calls to an [API Gateway](https://aws.amazon.com/api-gateway/) endpoint will still accrue [costs (API Gateway)](https://aws.amazon.com/api-gateway/pricing/)
- Cognito and API Gateway are free if your account is less than 12 months old and you make less than:
  - 50 thousand Cognito requests
  - 1 million API Gateway calls
- Read more about the [free tier](https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=*all&awsf.Free%20Tier%20Categories=*all)
- You must edit the variables under the 'Configuration' comment in the code to suit your Cognito setup
