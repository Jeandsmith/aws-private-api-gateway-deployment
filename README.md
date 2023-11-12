# AWS ApiGateway Private Api Deployment

## Application Deployment

1. Run `npm add` to install CDK on the directory.
2. Run `npm run cdk -- bootstrap`
    - Make sure to paste your account credentials as __environmental variables__.
3. RUn `npm run build_layers` To install the lambda layers
4. Run `pip install -r re
5. Open `cdk.context.json` and configure as needed.
6. Run `npm run cdk -- deploy`.
7. Run `npm run cdk -- destroy --force` when ready to remove the deployment.

```json
{
    "vpcId": "" # Default -- A new VPC will be created if field is removed
}
```
