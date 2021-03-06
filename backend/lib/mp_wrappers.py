""" Boto3 client wrappers."""


def get_user(iam_client, user):
    """ Return specific user information"""
    return iam_client.get_user(UserName=user)


def list_users(iam_client):
    """ List all IAM users """
    return iam_client.list_users()['Users']


def list_user_policies(iam_client, user):
    """ List IAM user policies """
    return iam_client.list_user_policies(UserName=user)


def list_attached_user_policies(iam_client, user):
    """ List IAM user policies """
    return iam_client.list_attached_user_policies(UserName=user)


def describe_clusters(redshift_client):
    """ Get Redshift cluster info """
    return redshift_client.describe_clusters()


def list_access_keys(iam_client, user):
    """ List IAM access keys for a user """
    return iam_client.list_access_keys(UserName=user)
