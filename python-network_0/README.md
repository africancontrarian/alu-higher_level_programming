# Python - Network #0

HTTP fundamentals via `curl`: request methods, headers, status codes,
query/POST parameters, and JSON request bodies, all against a local
web server on port 5000.

## Requirements

- Ubuntu 20.04 LTS
- Every script is exactly 3 lines (`#!/bin/bash`, a comment, the command),
  executable, and ends with a newline
- Every `curl` call uses `-s` (silent mode)

## Files

| File                    | Contents                                                          |
|--------------------------|------------------------------------------------------------------|
| `0-body_size.sh`         | Size (in bytes) of a response body                                |
| `1-body.sh`              | Response body, only for a `200` status                            |
| `2-delete.sh`             | `DELETE` request, displays the response body                      |
| `3-methods.sh`            | All HTTP methods a server accepts (`OPTIONS` + `Allow` header)     |
| `4-header.sh`             | `GET` request with a custom `X-HolbertonSchool-User-Id: 98` header |
| `5-post_params.sh`       | `POST` request with `email` and `subject` params                  |
| `100-status_code.sh`     | Only the response status code, no pipes/redirection/`;`/`&&`      |
| `101-post_json.sh`       | `POST` request with a JSON file's contents as the body             |
| `102-catch_me.sh`        | Requests `0.0.0.0:5000/catch_me`, letting `curl` print the body    |
