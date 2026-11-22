# Public Experience: Permissions and Security

## Service boundary

This repository describes the AWKH official shared MCP experience service. After OAuth authorization, the service exposes tools within the authenticated account and tenant scope.

The customer self-hosted edition is a separate product line. It runs its own Core, MCP service, database, credentials, and device scope on infrastructure controlled by the customer.

## Device authorization

- Connect only devices you own or are explicitly authorized to manage.
- New device enrollment may require approval by the tenant Owner.
- MCP client authorization and Agent device enrollment are separate processes.
- A pending registration, successful installer run, or OAuth connection alone does not mean the device is ready for management.
- Verify registration, approval where required, online heartbeat, and task results.

## Protect credentials

Never publish any of the following in GitHub Issues, discussions, screenshots, or chat messages:

- OAuth access or refresh tokens
- Agent enrollment invitations or one-time authorization codes
- Device tokens or API keys
- Passwords, private keys, or certificate private keys
- Production databases, customer records, or sensitive device output

If a credential may have been exposed, revoke or rotate it in the relevant service. Deleting a public message does not invalidate a credential.

## Hosted experience

The public shared service is provided for testing and evaluation. Review the sensitivity and impact of each operation before connecting a device. Do not use the hosted experience for critical production workloads without an independent security and operational assessment.

Available tools, permissions, quotas, and trial policies are determined by the service at the time of use.
