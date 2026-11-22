# AWKH Official MCP Quick Start

## Official connection address

`https://mcp.awkh.art/connect/mcp`

This is the MCP endpoint for the Alibaba-hosted official shared experience service. The website `https://agent.awkh.art/` is the product website, not the MCP endpoint. Singapore private QA endpoints are not public onboarding addresses.

## Connect from ChatGPT

1. Open ChatGPT on the web or desktop.
2. Open the app, connector, or custom MCP server settings (menu names may vary by client version).
3. Add a custom MCP server named AWKH.
4. Enter `https://mcp.awkh.art/connect/mcp` as the server URL.
5. Select OAuth and keep the client's default OAuth settings.
6. Save and complete authorization on the AWKH domain.

You do not need to manually enter an API key, platform administrator password, or device token. Never copy credentials or invitation tokens from another user.

## After connecting

Try asking:

- “Show the AWKH help information and explain the capabilities available to my account.”
- “Check my MCP connection status and explain how to enroll my own Windows device.”
- “List the prerequisites for connecting a device.”

## Enroll your own device

1. Identify whether the target device runs Windows or Linux.
2. Ask AWKH to generate the onboarding instructions for your account and operating system.
3. Run the installation command only on a device you own or are explicitly authorized to administer.
4. Check the device registration status in the MCP client. If approval is required, follow the Owner approval flow.
5. Confirm that the device is online and its status can be read before treating onboarding as complete.

An installer finishing successfully does not by itself prove that the Agent has registered, received authorization, or started sending heartbeats.

## Common states

- `401 Unauthorized` before OAuth is completed: expected for a protected MCP endpoint.
- MCP connected but no device appears: check Agent installation, registration, and any required Owner approval.
- Installer succeeded but device is offline: inspect the Agent service and registration/heartbeat status.

More information: <https://agent.awkh.art/>
