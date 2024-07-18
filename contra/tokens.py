from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six

class CustomTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.fecha_registro)
        )

custom_token_generator = CustomTokenGenerator()