from aws_cdk import (core as cdk, aws_ec2 as ec2, aws_ecs as ecs, aws_ecs_patterns as ecs_patterns)


class ProdEcsConstructStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        vpc = ec2.Vpc(self, "prod-vpc", max_azs=3)
        cluster = ecs.Cluster(self, "prod-cluster", vpc = vpc)
        ecs_patterns.ApplicationLoadBalancedFargateService(self, "Prod-Fargate-Service", cluster = cluster, desired_count = 2, cpu = 512, memory_limit_mib = 2048, task_image_options = ecs_patterns.ApplicationLoadBalancedTaskImageOptions(image = ecs.ContainerImage.from_registry("public.ecr.aws/t2u6r1h4/my-app")).add_port_mappings(ecs.PortMapping(container_port=5000, host_port = 80)), public_load_balancer = True)
