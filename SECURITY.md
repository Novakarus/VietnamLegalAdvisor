# Security Policy

This policy applies to the Vietnam Legal Advisor plugin source, the website, the packaging tools and the GitHub Actions workflows in this repository. Point of contact: Thanh Nguyen.

## Supported Versions

Only the latest released version is prioritized for security fixes. When a newer version replaces it, users should update; the project does not commit to maintaining separate patches for old versions.

| Version / component | Security support |
| --- | --- |
| Plugin 0.70.2 — candidate, not yet public | :white_check_mark: |
| Plugins before 0.70.2 | :x: |
| Website and tooling on the `main` branch | :white_check_mark: |

"Supported" means that reports are received, assessed and handled with appropriate priority; it is not a safety certification or a commitment to a remediation deadline. Version 0.70.2 is a candidate and is not public.

## Reporting a Vulnerability

**Please report privately by email: ntthanh912@gmail.com**, with the subject `[Security] Vietnam Legal Advisor — short description`.

Do not post unresolved vulnerabilities, credentials or sensitive data in Issues, Pull Requests or public discussions.

A report should include:

- The plugin version or commit hash, and the affected component and environment.
- A description of the issue, the conditions under which it occurs and its possible impact.
- Minimal reproduction steps using simulated data.
- Expected and actual results; evidence with sensitive information redacted.
- How to contact you and whether you wish to be credited, if applicable.

Issues that should be reported include disclosure of data or secrets; unauthorized access or actions; untrusted content that causes the assistant to cross permitted boundaries with a concrete security impact; and malicious code or interference with the website, release packages or packaging process.

Legal-answer errors, missing sources or interface bugs can be sent through Issues after removing sensitive information. If a bug also has a security impact, use the private email.

**Expected response process:**

- Target: acknowledge receipt within **5 working days**.
- Target: provide an initial assessment or request more information within **10 working days**.
- For a report being handled, target an update at least every **14 days**, even when there is no fix yet.

These are targets for a personally maintained project, not guaranteed deadlines. If you have not received an acknowledgement after 5 working days, you may send a reminder.

If a report is accepted, the Publisher will discuss the scope of impact, mitigations, the fix plan and an appropriate disclosure time. If the evidence is insufficient, the report is a duplicate or it is not confirmed as a vulnerability, the Publisher will explain the reason to the extent possible and will accept additional evidence.

Test only within the scope you are entitled to. Do not access other people's data, disrupt services or test third-party systems without permission. Issues belonging to the hosting platform, GitHub or the model provider should also be reported through the respective party's security channel.

The project does not have a bug bounty program. Reporters are credited only with their consent.
