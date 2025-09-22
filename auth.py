def authenticate(token):
    # Dummy IAM-style token check
    valid_tokens = ['tenant123-token', 'admin456-token']
    return token in valid_tokens
