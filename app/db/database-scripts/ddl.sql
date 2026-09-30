CREATE TABLE users (
    user_id UUID PRIMARY KEY,

    email VARCHAR(50),
    username VARCHAR(50),
    password_hash VARCHAR(100),

    is_active BOOLEAN,

    created_at TIMESTAMPTZ,
    updated_at TIMESTAMPTZ,
    last_login_at TIMESTAMPTZ,

    is_verified BOOLEAN,
    verified_at TIMESTAMPTZ
);