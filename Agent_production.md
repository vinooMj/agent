Everyone talks about agent intelligence. Then agents reach production - or face even the slightest bit of load - and suddenly the hard problems are:

- memory management
- concurrency
- backpressure
- retries
- timeouts
- failure handling
- observability

Agentic loops are long-running, non-deterministic, and inherently error-prone, which makes reliability difficult. The more complex the agents, the more interesting the failure modes.

Turns out, agents are often more of a classic software engineering problem than an AI problem. Good engineering practices are not going anywhere.
