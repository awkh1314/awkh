# Changelog

All notable public experience and documentation changes are recorded here. Internal Core, MCP, and Agent component versions are tracked separately in the private engineering repository.

## [0.1.0-preview] - 2026-11-22

First versioned public experience documentation release.

### Added
- Official public MCP endpoint: `https://mcp.awkh.art/connect/mcp`.
- OAuth-based ChatGPT/custom MCP connection instructions.
- Device onboarding guidance and registration/approval caveats.
- Public feature overview and security guidance.
- Clear separation between the AWKH-operated shared experience service and customer self-hosted private deployments.

### Scope
- Documentation and public onboarding information only.
- No proprietary server source, customer-private deployment package, or binary Agent installer is distributed by this release.
- Hosted service remains a testing/evaluation service; this release does not claim production GA status.

### Known limitations
- Available tools and quotas depend on the account's current server-side permissions and service policy.
- Device onboarding may require Owner approval; successful MCP OAuth connection or installer completion alone does not prove a device is online.
- Private deployment remains a separate preview product line and is not offered through this public repository.
