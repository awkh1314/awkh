# Public Release Policy

## Version ownership

The public experience version tracks what an external user can connect to and the public onboarding/documentation contract. It does not mirror the internal Core, MCP, Windows Agent, or Linux Agent versions.

## Release stages

- **Preview (0.x):** available for evaluation; functionality, permissions, quotas, and instructions may change.
- **Stable (1.x):** only after public connection, OAuth, device onboarding, security boundaries, and documented workflows pass release acceptance.
- **Hotfix:** increment the patch version and describe the user-visible correction.

## Automated release gate

The `.github/workflows/public-release.yml` workflow runs validation on pushes to `main` and pull requests targeting `main`. It checks:

1. SemVer syntax and consistency between `VERSION`, `CHANGELOG.md`, `RELEASES.md`, and the versioned release notes.
2. The official public MCP endpoint in the README, quick-start guide, and release notes.
3. Required public documentation and release metadata.
4. Tracked paths for private platform/deployment content and binary packages.
5. Common credential patterns, private QA hostnames, and whitespace errors.

To publish a release, open **Actions → AWKH public release gate → Run workflow**, select branch `main`, enter the exact version from `VERSION`, and select whether the release is a pre-release. The publish job runs only after validation passes. It creates or verifies the matching `v<version>` tag and creates or updates the GitHub Release from `releases/v<version>.md`.

The workflow requires GitHub Actions to be enabled and the repository's Actions token to have `contents: write` permission. It publishes documentation/hosted-experience notes only; it does not deploy production services or upload private binaries.

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
