# Architectural Guideline: 10 Core Concepts for Low Cognitive Load & AI-Agentic Alignment

This guideline establishes our team’s engineering standard. Its dual objective is to minimize **Human Cognitive Load** (preventing developer burnout and tracking fatigue) and maximize **LLM/AI Agent Performance** (ensuring tools like Claude Code, Cursor, and OMO frameworks write flawless code with minimal tokens and zero hallucinations).

---

## Quick Reference Cheat Sheet

| #      | Concept                                 | Human Cognitive Benefit                              | AI-Agentic Benefit                                            |
| ------ | --------------------------------------- | ---------------------------------------------------- | ------------------------------------------------------------- |
| **1**  | **Deep Modules**                        | Mental isolation; details are hidden.                | Prevents token spill from unrelated implementation code.      |
| **2**  | **Schema-Driven / Contract-First**      | Explicit boundaries reduce integration guesswork.    | Gives the AI strict mathematical guardrails to fill in.       |
| **3**  | **Strict Compile-Time Guarantees**      | Eradicates runtime surprises; immediate feedback.    | Enables the AI's autonomous LSP "auto-heal" loop.             |
| **4**  | **Convention over Innovation**          | Eliminates learning curves for shared codebases.     | Leverages the LLM’s highest statistical training weights.     |
| **5**  | **Strict Context-Window Optimization**  | Files are scannable in under 10 seconds.             | Eliminates attention decay and "needle-in-a-haystack" issues. |
| **6**  | **Explicit over Implicit (Anti-Magic)** | Tracing dependencies requires zero magical thinking. | Maximizes static analysis capability for AI code parsing.     |
| **7**  | **Exhaustive Error Types**              | Forces developers to handle edge cases explicitly.   | Eliminates AI guesswork on what a service might return.       |
| **8**  | **Semantic Token Optimization**         | Self-documenting code; names declare intention.      | Enhances LLM vector embedding and reasoning alignment.        |
| **9**  | **Pure Functions & Immutability**       | Logic is deterministic; zero hidden side effects.    | Simplifies isolated automated unit-test generation.           |
| **10** | **Linear Execution (The Bouncer)**      | Flattened logic eliminates indentation tracking.     | Minimizes logical combinatorial explosion paths ($2^n$).      |

---

## Detailed Summary of the 10 Concepts

### 1. Deep Modules

- **The Philosophy:** A module should have a highly simple, abstract public interface (API) but encapsulate significant, complex internal functionality. The opposite is a "shallow module," which forces developers to see or manage internal implementation details.
- **Human Impact:** You can understand and call a module with minimal mental overhead. You don't have to think about _how_ it works, only _what_ it does.
- **AI Impact:** By exposing only a clean public interface (via an explicit `index.ts` or a NestJS `@Module` export block), the AI agent does not read or parse thousands of lines of helper functions unless it is explicitly assigned to modify that exact deep internal folder.
- **Rule of Thumb:** Make interfaces simple; hide the implementation details inside private local sub-folders or files.

### 2. Schema-Driven / Contract-First Development

- **The Philosophy:** Define data models, validation layer parameters, and network interfaces (Prisma schemas, OpenAPI/Swagger specifications, Zod schemas) before writing any application handlers.
- **Human Impact:** Developers on both the frontend (React) and backend (NestJS) possess an immediate, unyielding source of truth regarding how data moves through systems.
- **AI Impact:** LLMs excel at "filling in code" when bounded by explicit mathematical rules. Providing a complete data schema drastically slashes AI code generation syntax errors on the first attempt.
- **Rule of Thumb:** Define the data shape or API contract in code _first_, then derive TypeScript types and application logic directly from it.

### 3. Strict Compile-Time Guarantees (Total Type Safety)

- **The Philosophy:** Treat compiler warnings as fatal errors. Eradicate any use of the `any` keyword, loose type coercion (`as unknown as Type`), or optional chaining bypasses where explicit handling is required.
- **Human Impact:** Catching architectural breakages during the compilation step eliminates tedious, time-consuming runtime browser testing or server debugging sessions.
- **AI Impact:** When an AI agent introduces a bug, a strict TypeScript configuration (`tsconfig.json`) fails instantly. The Language Server Protocol (LSP) flags the line, allowing agentic loops to parse the error message and auto-heal their own code errors without human intervention.
- **Rule of Thumb:** If it cannot be checked by the compiler statically at build-time, rewrite the implementation to ensure it can.

### 4. Convention Over Custom Innovation

- **The Philosophy:** Prioritize standard ecosystem frameworks, architectural guidelines, and idiomatic library patterns over customized internal wrappers.
- **Human Impact:** Onboarding a engineer requires minimal internal documentation; if they know NestJS or TanStack Query, they immediately understand the codebase.
- **AI Impact:** AI model intelligence is directly tied to standard internet training documentation. Utilizing hyper-custom architectural wrappers breaks the AI’s statistical training advantages, inducing hallucinations.
- **Rule of Thumb:** Do not write custom internal framework wrappers. Follow native framework documentation exactly.

### 5. Strict Context-Window Optimization (Small File Boundaries)

- **The Philosophy:** Impose strict operational caps on individual file lengths (e.g., a maximum limit of 150 to 200 lines of code per file).
- **Human Impact:** Prevents "scroll-blindness," allowing developers to read and understand a file's intent in under 10 seconds.
- **AI Impact:** Long files saturate the LLM's context window, degrading its focus (the attention drop-off effect). Small, single-responsibility files consume far fewer tokens and allow rapid, precise agent processing.
- **Rule of Thumb:** The moment a file exceeds 150 lines, slice out internal UI elements or domain calculators into separate, colocated files in the same directory.

### 6. Explicit over Implicit (Anti-Magic)

- **The Philosophy:** Avoid advanced metaprogramming, dynamic runtime string parsing to identify methods, or hidden global behaviors. Execution paths, parameters, and imports must be literal and statically discoverable.
- **Human Impact:** Code behaves predictably. A developer can use their IDE's "Go to Definition" feature to trace execution, without needing deep structural tribal knowledge.
- **AI Impact:** AI context parsers read code statically. Dynamic code generation hidden behind runtime reflection creates severe blind spots where the AI cannot see or trace software dependencies.
- **Rule of Thumb:** Code should be literal. Prefer verbose, visible imports and explicit function calls over automatic, implicit runtime configurations.

### 7. Exhaustive Error Types / Discriminated Unions

- **The Philosophy:** Avoid throwing untyped, generic errors. Instead, design complex execution services to return explicit success/failure shapes powered by a identifying type discriminator.
- **Human Impact:** Developers reading a function signature immediately see all possible business-logic failure modes without digging into lines of nested try/catch code.
- **AI Impact:** When an LLM reads a strict return signature type like `errorType: 'CLASS_FULL' | 'INSUFFICIENT_FUNDS'`, its generation weights are statistically forced to write client UI handlers for every single edge case scenario.
- **Rule of Thumb:** Reserve exception throwing for completely unexpected framework or system failures (e.g., DB disconnected). For predictable domain failures, return explicit object unions.

### 8. Semantic Token Optimization (Intention Naming)

- **The Philosophy:** Name components, functions, variables, and hooks with absolute clarity regarding their literal purpose, regardless of name length. Avoid cryptic, heavily truncated terms.
- **Human Impact:** Minimizes the cognitive deciphering stage when reading a teammate's pull request.
- **AI Impact:** LLMs navigate code repositories via semantic language embeddings. Highly clear, intention-revealing variable tokens drastically improve the AI's neural path navigation accuracy.
- **Rule of Thumb:** Prefer `useClassBookingRescheduleMutationHandler` over `useReschedule`. Clarity always trumps brevity.

### 9. Pure Functions & State Immutability

- **The Philosophy:** Segregate complex core calculations into pure mathematical functions (same input always produces the exact same output, with absolutely no external variables or mutations altered outside the function block).
- **Human Impact:** You can test, rewrite, and reason about core business mathematics without worrying about breaking state in distant, unrelated modules.
- **AI Impact:** LLMs easily lose track of complex state machines when they span asynchronous calls across multiple components. Pure functions allow AI agents to isolate logic and construct perfect automated unit tests.
- **Rule of Thumb:** Keep network and database actions decoupled from calculation formulas. Pass data into a pure function, receive the calculation result, and then apply state updates.

### 10. Linear Execution (The Bouncer Pattern)

- **The Philosophy:** Eradicate deeply nested conditional branches (`if/else` ladders) by implementing immediate, aggressive guard clauses at the absolute top of the function structure.
- **Human Impact:** Flattens the execution flow. Once a developer reads past a guard clause, they can completely eject that edge case scenario from their active working memory.
- **AI Impact:** Deeply nested code paths present an exponential tracking tree for code parsing. Keeping code strictly flat and linear ensures the AI can process logic flawlessly step-by-step.
- **Rule of Thumb:** "Bounce" invalid criteria out of the function immediately using early returns or clean exceptions at the top of the execution block. Keep the primary success logic entirely un-indented.
