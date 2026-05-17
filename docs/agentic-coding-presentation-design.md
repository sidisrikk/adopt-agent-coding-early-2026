# Agentic Coding Presentation Design

**Topic:** Adopting Agentic Coding
**Audience:** Mid-level Developers
**Duration:** 30 minutes
**Structure:** Big Picture to Daily Practice (Theory → Practice)

## Part 1: Concepts & Mechanics (15 minutes)

**Slide 1: Title & Goal**
*   **Topic:** Adopting Agentic Coding
*   **Key Point:** Moving beyond simple autocomplete to collaborative AI workflows.

**Slide 2: The Agent Capability Spectrum**
*   **Topic:** Where are we now, and where are we going?
*   **Content:** Briefly touch on L1 (Completion/Copilot) -> L2 (Chat) -> L3 (Command/Autonomous) -> L4 (Background).
*   **Key Point:** Most teams are at L2; we want to engineer our way to L3.

**Slide 3: The Engine - Context Windows**
*   **Topic:** How the AI "remembers".
*   **Content:** Explain Input + Output tokens. Introduce the "Lost in the Middle" problem visually (first and last messages have high impact, middle is easily forgotten).

**Slide 4: Managing the Engine - Token Efficiency**
*   **Topic:** Don't waste the context window.
*   **Content:** 
    *   *Caveman Interaction:* Short, clear, no fluff.
    *   *Sidenotes & Todo Tools:* Keeping the main context clean.
    *   *Cutover Context:* Wipe the slate clean when starting a new story.
    *   *Right Model for the Job:* Small vs. Large models.

**Slide 5: Orchestration & Subagents**
*   **Topic:** Why one big agent isn't enough.
*   **Content:** Explain dividing work: Orchestrator (planner) vs. Specialists (implement, debug, refactor).

## Part 2: Practice & Collaboration (15 minutes)

**Slide 6: Asynchronous Workflows**
*   **Topic:** How to work *with* the agent, not just wait for it.
*   **Content:** 
    *   *HITL (Human-in-the-Loop):* When to step in to approve or correct.
    *   *AFK (Away from Keyboard) Coding:* Setting up long tasks and letting them run.

**Slide 7: Team Collaboration & Artifacts**
*   **Topic:** How we share knowledge in the AI era.
*   **Content:** 
    *   Building Shared Skills for the squad (e.g., standard error handling).
    *   Machine-Readable Artifacts: Docs are for transferring understanding to agents and humans, not just checking a box.

**Slide 8: Ready-to-Use Skillsets**
*   **Topic:** Don't start from scratch.
*   **Content:** Highlight existing workflows (Implement, debug, refactor, test). Mention examples like Matt Pocock's skills or the Superpowers repo.

**Slide 9: The Agent Marketplace & Wrap-up**
*   **Topic:** Where to find more tools.
*   **Content:** Quick mention of marketplaces (skills.sh, gstack). Open for Q&A.