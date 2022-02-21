from aws_cdk import (
    aws_iam as iam,
)


def get_role(scope, profile_name, principal, policies_list, additional_policies=[]):
    role = iam.Role(
        scope,
        profile_name,
        role_name=f"{profile_name}_Aggregator",
        assumed_by=iam.ServicePrincipal(principal),
    )

    for policy in policies_list:
        role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name(policy))

    if additional_policies:
        role.add_to_policy(
            iam.PolicyStatement(
                resources=["*"],
                actions=additional_policies,
                effect=iam.Effect.ALLOW,
            )
        )

    return role
