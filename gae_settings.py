from django_openid_auth.models import Association, UserOpenID

FIELD_INDEXES = {
    Association: {'indexed': ['server_url']},
    UserOpenID: {'indexed': ['claimed_id']},
}
