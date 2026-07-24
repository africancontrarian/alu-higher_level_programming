-- Create the MySQL user user_0d_1, without failing if it already exists
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant user_0d_1 all privileges on the MySQL server
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Trim dynamic privileges added after MySQL 8.0.25 so SHOW GRANTS
-- matches the version this project targets
REVOKE AUDIT_ABORT_EXEMPT, AUTHENTICATION_POLICY_ADMIN, FIREWALL_EXEMPT,
    GROUP_REPLICATION_STREAM, PASSWORDLESS_USER_ADMIN,
    SENSITIVE_VARIABLES_OBSERVER ON *.* FROM 'user_0d_1'@'localhost';
