from aws_cdk import (
    Stack,
)
from constructs import Construct
from aws_cdk.aws_apigateway import (
    RestApi,
    EndpointConfiguration,
    StageOptions,
    EndpointType,
    MockIntegration,
    IntegrationResponse,
    MethodOptions,
    MethodResponse,
)
from aws_cdk.aws_iam import (
    PolicyStatement,
    AnyPrincipal,
    Effect,
    PolicyDocument,
)
from aws_cdk.aws_ec2 import Vpc, InterfaceVpcEndpointAwsService


class AwsStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Getting the User provided VPC ID
        vpc_id: str | None = self.node.try_get_context("vpcId")

        # Either import or create the VPC
        vpc = (
            Vpc(self, "vpc", vpc_name="private-api-vpc")
            if not vpc_id
            else Vpc.from_lookup(self, "vpc", vpc_id=vpc_id)
        )

        # Add the APIGW VPC Endpoint to set the endpoint as private
        vpc_endpoint = vpc.add_interface_endpoint(
            "api-interace",
            service=InterfaceVpcEndpointAwsService.APIGATEWAY,
            private_dns_enabled=True,
        )

        # Policy telling us that only resources coming through the vpc endpoint can execute our apu
        policy = PolicyDocument(
            statements=[
                PolicyStatement(
                    principals=[AnyPrincipal()],
                    actions=["execute-api:Invoke"],
                    resources=[
                        Stack.of(self).format_arn(service="execute-api", resource="*")
                    ],
                    effect=Effect.ALLOW,
                    conditions={
                        "StringEquals": {"aws:SourceVpce": vpc_endpoint.vpc_endpoint_id}
                    },
                )
            ],
        )

        # Our rest api
        api = RestApi(
            self,
            "private-api",
            deploy=True,
            deploy_options=StageOptions(stage_name="dev"),
            policy=policy,
            endpoint_configuration=EndpointConfiguration(types=[EndpointType.PRIVATE]),
            default_integration=MockIntegration(
                request_templates={
                    "application/json": "{statusCode: 200}",
                },
                integration_responses=[
                    IntegrationResponse(
                        status_code="200",
                    ),
                ],
            ),
            default_method_options=MethodOptions(
                method_responses=[MethodResponse(status_code="200")]
            ),
        )

        api.root.add_proxy(any_method=True)
