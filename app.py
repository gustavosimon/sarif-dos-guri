DB_HOST = 'production.cnvs.com'
DB_PORT = 5432
DB_USER = 'cnvs-db-prod'
DB_PASS = '8d6c29ac-eb3e-42f9-86d7-f3507fe0f508'


def login(email, password):
    db_connection = DatabaseConnection(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASS
    )

    user = db_connection.execute(
        f"SELECT * FROM accounts WHERE email = '{email}' AND password = '{password}' "
    )

    if not user:
        return None
    
    token = generate_session_token(user)

    return user, token