# AWKH

**AI-agent-powered device management and automation through MCP.**

AWKH connects an AI assistant to devices you own or are explicitly authorized to manage. It provides a structured way to inspect capabilities, plan actions, execute tasks, and verify results.

- Website: <https://agent.awkh.art/>
- **Official public MCP endpoint:** <https://mcp.awkh.art/connect/mcp>
- Authentication: OAuth
- Current public experience version: [`0.1.0-preview`](releases/v0.1.0-preview.md)

## What it does

- **Device management** — inspect and manage enrolled Windows and Linux devices within your authorized scope.
- **MCP integration** — connect compatible AI clients to AWKH device capabilities.
- **Multiple execution modes** — command-line, background automation, and interactive GUI workflows, depending on Agent capabilities.
- **Task verification** — track execution status and verify outcomes instead of treating command dispatch as success.
- **Private deployment** — run a separate, self-hosted instance for your own devices.

## Getting started

1. Open ChatGPT or another compatible MCP client.
2. Add a custom MCP server using `https://mcp.awkh.art/connect/mcp`.
3. Select OAuth and complete authorization on the AWKH domain.
4. Ask AWKH for the device onboarding instructions for your operating system.
5. Install the Agent only on a device you own or are authorized to manage, then verify its registration and online status.

See the [quick-start guide](docs/quick-start.md), [feature overview](docs/experience.md), and [security notes](docs/privacy-and-safety.md).

## Releases and updates

- [Latest public experience release](RELEASES.md)
- [Changelog](CHANGELOG.md)
- [Release policy](docs/release-policy.md)

The public experience version is independent of the internal AWKH Core, MCP, and Agent component versions. A documentation/experience release does not imply that downloadable binaries or proprietary server source are published.

## Official shared service and private deployment

The public endpoint above connects to the AWKH-operated shared experience service. A customer's private deployment is a separate product line: it runs its own Core, MCP service, database, credentials, and device scope on infrastructure controlled by that customer. Private deployment source and packages are not published in this repository.

## Project status

AWKH is under active development. The hosted public service is provided for testing and evaluation. Do not treat it as a production security guarantee or connect devices containing sensitive workloads without independently reviewing the risks.

## Security

- Only connect devices you own or have explicit permission to administer.
- MCP client authorization and Agent device enrollment are separate steps. A successful OAuth connection does not mean a device is enrolled or online.
- Do not publish access tokens, refresh tokens, device invitations, passwords, private keys, certificates, or customer data in issues or discussions.
- Report suspected vulnerabilities privately through the project's website contact channel.

## Source and licensing

The proprietary AWKH Core, MCP service, and private-delivery implementation are maintained in a separate private repository. Public visibility of this repository does not grant a license to copy, modify, redistribute, or resell AWKH software.

Copyright (c) 2026 AWKH. All rights reserved.
