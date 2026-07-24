# Python - Network #1

Fetching and manipulating HTTP resources from Python, first with the
standard-library `urllib` package, then with the third-party `requests`
package: GET/POST requests, response headers, error handling, and JSON.

## Requirements

- Ubuntu 14.04 LTS, python3 (3.4.3), PEP 8 (pycodestyle 1.7)
- Every file starts with `#!/usr/bin/python3`, is executable, and ends
  with a newline
- Every module has a real documentation sentence
- No code runs on import (`if __name__ == "__main__":`)
- Dictionary values are accessed with `.get()`

## Files

| File                    | Contents                                                          |
|--------------------------|--------------------------------------------------------------------|
| `0-hbtn_status.py`       | Fetches the ALU status endpoint with `urllib`                     |
| `1-hbtn_header.py`       | `X-Request-Id` response header, via `urllib`                       |
| `2-post_email.py`        | `POST` with an `email` param, via `urllib`                         |
| `3-error_code.py`        | Prints the body, or `Error code: <n>` on `urllib.error.HTTPError`  |
| `4-hbtn_status.py`       | Fetches the ALU status endpoint with `requests`                    |
| `5-hbtn_header.py`       | `X-Request-Id` response header, via `requests`                     |
| `6-post_email.py`        | `POST` with an `email` param, via `requests`                       |
| `7-error_code.py`        | Prints the body, or `Error code: <n>` for a 400+ status            |
| `8-json_api.py`          | Searches `search_user` by letter, handles invalid/empty JSON       |
| `10-my_github.py`        | GitHub user id via Basic Authentication                            |
| `100-github_commits.py`  | Lists the 10 most recent commits of a GitHub repository            |
