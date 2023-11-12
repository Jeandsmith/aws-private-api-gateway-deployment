# AWS ApiGateway Private Api Deployment

## Application Deployment

1. Run `npm add` to install CDK on the directory.
2. Run `npm run cdk -- bootstrap`
    - Make sure to paste your account credentials as __environmental variables__.
3. Run `cd app`
4. Run `python -m venv .venv`
5. Run `.venv/[bin or Script]/activate`
6. Open `cdk.context.json` and configure as needed.
7. Run `npm run deploy`.
8. Run `npm run cdk -- destroy --force` when ready to remove the deployment.

```python
{
    "vpcId": "" # Default -- A new VPC will be created if field is removed
}
```
