# The agent capability spectrum

Not all agents are created equal. The capability spectrum ranges from simple assistants to fully autonomous systems, and understanding where your agents fall on this spectrum determines the engineering requirements.

Level 1: Completion agents suggest code as you type. They operate within the IDE, have no access to external tools, and produce output that the developer reviews character by character. GitHub Copilot’s inline suggestions are the canonical example. The engineering requirements are minimal - the IDE handles the integration, and the developer is the quality gate.

Level 2: Chat agents respond to natural language requests within a conversation. They can generate multi-line code, explain concepts, and answer questions about the codebase. They operate within a chat interface and produce output that the developer copies into their code. The engineering requirements are moderate - you need to manage context (what files are included in the conversation) and review output before using it.

Level 3: Command agents execute actions in the development environment. They can read and write files, run commands, create branches, and open pull requests. They operate autonomously within a session, making decisions about what to do next based on the results of their actions. Claude Code, Cursor’s agent mode, and Ona are examples. The engineering requirements are significant - you need authorization (what can the agent do?), observability (what did the agent do?), and cost control (how much did it spend?).

Level 4: Background agents run without human supervision. They monitor repositories for issues, automatically fix bugs, generate tests, update documentation, and create pull requests - all without a human initiating the task. GitHub Agentic Workflows and scheduled agent tasks are examples. The engineering requirements are the highest - you need everything from Level 3 plus automated quality gates, kill switches, and incident response procedures.

Most teams in February 2026 are at Level 2-3. The transition from Level 2 to Level 3 is where the engineering discipline of this guide becomes essential. The transition from Level 3 to Level 4 is where it becomes critical.
