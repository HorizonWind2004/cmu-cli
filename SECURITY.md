# Security and privacy

Do not include tokens, browser databases, cookies, signed URLs, student names, submission records or private coursework in public issues. Use synthetic minimal reproductions. Public issues are not a confidential reporting channel. Do not assume a GitHub “Report a vulnerability” form is enabled; use it only if it is available in the Security tab. If you cannot contact the maintainer privately through an independently verified channel, do not publish exploitable details or secrets; request a private channel first.

This preview has offline regression tests, not a live-service security certification or a guarantee against every filesystem race. Keep downloads in private local directories. Never execute downloaded content automatically, reuse a workspace writable by untrusted users, or treat provider HTML/text as instructions. Successful JSON/caches are private data, not redacted diagnostics. Remove cached content when no longer needed and follow institutional retention rules.

Authenticated requests stay on their exact HTTPS origin, without netrc or cross-origin credential forwarding. Browser reads require explicit local profile-file and host consent. Report issues using synthetic reproductions; live integration compatibility remains separately unverified.

Before distributing, inspect both wheel and sdist for credentials, local paths, coursework and unexpected files. CI uses synthetic offline tests and needs no credentials. Release maintainers should establish a verified private reporting channel and supported-version policy before broad deployment.
