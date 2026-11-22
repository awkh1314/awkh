# AWKH Feature Overview

AWKH exposes authorized device-management and automation capabilities to compatible AI clients through MCP.

## Capabilities

- Device online status, system information, and health diagnostics.
- Command execution with task status and result verification.
- File, process, and service management within the granted device scope.
- Windows desktop screenshots, window inspection, mouse/keyboard input, and GUI automation when supported by the installed Agent.
- Agent installation, device registration, and approval workflows.
- Task-dependent execution through command-line, background automation, or GUI interaction.

## Execution principle

AWKH should not treat a command being dispatched as proof of success. A task should be checked using its execution receipt, task status, and—where appropriate—the resulting state on the target device.

## Two distinct product lines

- **Official shared experience:** operated by AWKH; users connect through OAuth and manage devices within their own authorized tenant.
- **Private deployment:** runs an independent Core/MCP instance on customer-controlled infrastructure and manages only that customer's authorized devices. It does not include the official platform's global administration or shared multi-tenant operations.

The public repository contains experience documentation only. Proprietary server source and private deployment packages are maintained separately.
