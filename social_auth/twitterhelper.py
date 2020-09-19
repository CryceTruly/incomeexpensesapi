import twitter
import os
from rest_framework import serializers


class TwitterAuthTokenVerification:
    """
    class to decode user access_token and user access_token_secret
    tokens will combine the user access_token and access_token_secret
    separated by space
    """

    @staticmethod
    def validate_twitter_auth_tokens(access_token_key, access_token_secret):
        """
        validate_twitter_auth_tokens methods returns a twitter
        user profile info
        """

        consumer_api_key = os.environ.get('TWITTER_API_KEY')
        consumer_api_secret_key = os.environ.get('TWITTER_CONSUMER_SECRET')

        try:
            api = twitter.Api(
                consumer_key=consumer_api_key,
                consumer_secret=consumer_api_secret_key,
                access_token_key=access_token_key,
                access_token_secret=access_token_secret
            )

            user_profile_info = api.VerifyCredentials(include_email=True)
            return user_profile_info.__dict__

        except Exception as identifier:

            raise serializers.ValidationError({
                "tokens": ["The tokens are invalid or expired"]})
