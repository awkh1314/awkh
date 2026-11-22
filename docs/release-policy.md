# Public Release Policy

## Version ownership

The public experience version tracks what an external user can connect to and the public onboarding/documentation contract. It does not mirror the internal Core, MCP, Windows Agent, or Linux Agent versions.

## Release stages

- **Preview (0.x):** available for evaluation; functionality, permissions, quotas, and instructions may change.
- **Stable (1.x):** only after public connection, OAuth, device onboarding, security boundaries, and documented workflows pass release acceptance.
- **Hotfix:** increment the patch version and describe the user-visible correction.

## Every release must record

1. Public experience version and release date.
2. Public MCP endpoint and authentication method.
3. User-visible additions, changes, and fixes.
4. Required client/Agent compatibility, where applicable.
5. Known limitations and security notices.
6. Whether the release contains documentation only, source, or downloadable binaries.
7. Checksums for every distributed binary artifact.

## Publication boundary

This public repository may contain product descriptions, connection instructions, release notes, and public troubleshooting documentation.

It must not contain:
- Official platform proprietary source.
- Private-deployment source or deployment bundles.
- Customer databases, logs, credentials, tokens, or enrollment invitations.
- Private QA hostnames or private test-only endpoints.

## Promotion to stable

Do not mark a release Stable/GA solely because a Git commit or documentation update succeeded. Require verified OAuth connection, onboarding of authorized test devices, registration/approval/heartbeat checks, representative task execution, security review, and recovery/rollback checks.
