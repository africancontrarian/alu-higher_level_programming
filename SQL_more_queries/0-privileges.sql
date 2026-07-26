-- List all privileges of the users user_0d_1 and user_0d_2 on localhost.
-- The dynamic privileges introduced after MySQL 8.0.25 are dropped
-- first so the SHOW GRANTS output matches the version this project
-- targets. Each user is trimmed and displayed in turn so the first
-- listing is always produced even if a user has nothing to trim.
REVOKE AUDIT_ABORT_EXEMPT, AUTHENTICATION_POLICY_ADMIN, FIREWALL_EXEMPT,
    GROUP_REPLICATION_STREAM, PASSWORDLESS_USER_ADMIN,
    SENSITIVE_VARIABLES_OBSERVER, TELEMETRY_LOG_ADMIN
    ON *.* FROM 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_1'@'localhost';
REVOKE AUDIT_ABORT_EXEMPT, AUTHENTICATION_POLICY_ADMIN, FIREWALL_EXEMPT,
    GROUP_REPLICATION_STREAM, PASSWORDLESS_USER_ADMIN,
    SENSITIVE_VARIABLES_OBSERVER, TELEMETRY_LOG_ADMIN
    ON *.* FROM 'user_0d_2'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
