Here is a concise, executive summary designed for your squad team presentation. It pitches the architectural pivot to an **AI-First, Feature-Based Structure**, focusing on why it reduces cognitive load for both human engineers and AI coding agents.

---

# Executive Summary: Front-End Architecture Selection for Next Project

## 1. The Core Paradigm Shift: AI-First Development

When choosing our next project's code structure, we must optimize for **two types of developers**: our human squad and our AI coding agents (Cursor, Claude Code, etc.).

To maximize velocity, our architecture must champion **Low Cognitive Load** and **Context Localization**. AI agents do not navigate apps like humans; they rely on token context windows, file tree traversals, and tool calls. A fragmented codebase forces the AI to waste tokens, lose focus, and hallucinate paths.

---

## 2. Technical Options Comparison

| Architecture | Scaling Ability | AI Agent Compatibility | Main Bottleneck for AI / Squad |
| ------------ | --------------- | ---------------------- | ------------------------------ |
| **Folder by Type** (components/, hooks/)  | Poor | **Low** | **High Folder Hopping:** Forces AI to execute multiple tool calls across scattered folders to change one feature. |
| **Atomic Design** (atoms/, molecules/) | Medium | **Low** | **Subjective Boundaries:** Constant bikeshedding over what is a molecule vs. organism; confuses AI rules. |
| **Feature-Sliced Design** (entities/, features/) | Enterprise | **Medium** | **Token Bloat:** High abstraction and deep splitting over-engineer simple tasks, draining token windows. |
| **Feature-Based (Modular)** (features/[domain]/) | High | **Excellent (The Winner)** | Requires developer discipline to maintain strict entry points (`index.ts`) and clean shared folder boundaries. |

---

## 3. Why Feature-Based (Modular) Layout Wins

### 🚀 Context Localization (Token Efficiency)

Everything required to run a business domain (UI components, custom hooks, data-fetching services, types) is colocated inside a single feature folder. When an AI agent needs to modify a feature, it reads one self-contained directory instead of dragging the whole repo into its context window.

### 🛡️ Strict Entry Gates (`index.ts` Guardrails)

Each feature exposes its public API through a root `index.ts` file.

- Humans and AI agents are **only** allowed to import from this gate.
- It stops the AI from creating fragile, deep-nested cross-feature imports and prevents spaghetti code.

### 🧹 Clean Separation of UI Primitives

Global UI components (`src/components/ui/`) are kept entirely stateless and free of business context (e.g., raw buttons, inputs). All smart, domain-specific UI logic is forced to live strictly within its designated feature module.

---

## 4. The Proposed Blueprint

```text
src/
├── app/                            # Global Core & Config (The Shell)
│   ├── providers/
│   │   ├── AppProvider.tsx         # Combines all providers into a single wrapper tree
│   │   ├── MUIProvider.tsx         # Material UI Custom Theme overrides & Baseline
│   │   └── QueryProvider.tsx       # TanStack Query Client provider config
│   ├── routes/
│   │   └── router.tsx              # React Router definitions (createBrowserRouter config)
│   ├── App.tsx                     # Main App orchestration component
│   └── main.tsx                    # Vite Entrypoint
│
├── components/                     # Pure Global UI Primitives (MUI Theme Wrappers)
│   └── ui/
│       ├── ControlledInput.tsx     # Global wrapper combining React Hook Form + MUI TextField
│       ├── LoadingButton.tsx       # Custom MUI Button variant with an integrated spinner
│       └── StatusBadge.tsx         # MUI Chip component variant for consistent status pill styling
│
├── features/                       # Bounded Business Contexts (Low Cognitive Load Zone)
│   │
│   ├── class-booking/              # --- DOMAIN: CLASS BOOKING ---
│   │   ├── components/
│   │   │   ├── BookingCalendar.tsx # Complex UI grid for slots
│   │   │   └── BookingForm.tsx     # Main form file utilizing React Hook Form + MUI
│   │   ├── hooks/
│   │   │   ├── useBookings.ts      # TanStack useQuery (Fetch available slots/classes)
│   │   │   └── useCreateBooking.ts # TanStack useMutation (Dispatches new reservations)
│   │   ├── services/
│   │   │   └── bookingApi.ts       # Axios instance endpoints targeting /api/bookings
│   │   ├── types/
│   │   │   └── index.ts            # Booking & Class TS Interfaces
│   │   └── index.ts                # Public Gate (Exposes BookingCalendar, BookingForm, hooks)
│   │
│   ├── notifications/              # --- DOMAIN: NOTIFICATIONS ---
│   │   ├── components/
│   │   │   ├── NotificationBell.tsx# Header button displaying notification counts
│   │   │   └── NotificationList.tsx# Sidebar or Dropdown menu detailing alerts
│   │   ├── hooks/
│   │   │   └── useNotifications.ts # TanStack useQuery pulling system alerts or SSE hooks
│   │   ├── services/
│   │   │   └── notificationApi.ts  # Axios endpoints targeting /api/notifications
│   │   └── index.ts                # Public Gate
│   │
│   └── payments/                   # --- DOMAIN: PAYMENTS ---
│       ├── components/
│       │   ├── CheckoutForm.tsx    # Stripe/Gateway form elements wrapped in React Hook Form
│       │   └── PaymentHistory.tsx  # Interactive MUI DataGrid rendering transaction records
│       ├── hooks/
│       │   └── useProcessPayment.ts# TanStack useMutation communicating with payment gateway
│       ├── services/
│       │   └── paymentApi.ts       # Axios endpoints targeting /api/payments
│       └── index.ts                # Public Gate
│
├── hooks/                          # Global, Non-Domain Core React Hooks
│   ├── useAuth.ts                  # Application auth session hook
│   └── useDebounce.ts              # Search input optimization helper
│
├── lib/                            # Core Infrastructure SDK Configurations
│   ├── apiClient.ts                # Configured Axios instance with interceptors for JWT injection
│   └── queryClient.ts              # Master TanStack QueryClient setup configurations
│
├── pages/                          # --- THE COMPOSITION LAYER (Where page.tsx lives) ---
│   ├── layout.tsx                  # Base UI Blueprint layout (Shared Navbar, Sidebar, & React Router <Outlet />)
│   ├── dashboard/
│   │   └── page.tsx                # Route: /dashboard (Combines general stats & NotificationBell)
│   ├── bookings/
│   │   ├── page.tsx                # Route: /bookings (Renders <BookingCalendar /> from features)
│   │   └── [id]/
│   │       └── page.tsx            # Route: /bookings/:id (Renders specific booking details view)
│   ├── payments/
│   │   └── page.tsx                # Route: /checkout (Renders <CheckoutForm /> from features)
│   └── error-page.tsx              # App-wide Router Error Boundary view
│
└── utils/                          # Pure, Stateless Utility Helpers
    └── formatters.ts               # formatCurrency (THB/USD), formatDate (using dayjs)
```

---

## 5. Implementation Roadmap for the Squad

If we choose the **Feature-Based Layout**, we will enforce three configuration guardrails on day one:

1. **Absolute Imports:** Configure `tsconfig.json` paths (`@/features/*`) to eliminate ugly relative path resolution (`../../../../`) which AI agents easily break.
2. **AI Optimization Rules:** Commit a `.cursorrules` or `ai-settings.md` to the root folder explicitly instructing AI agents to adhere strictly to our feature isolation rules and use the `index.ts` gates.
3. **Strict Code Reviews:** Ensure the `shared/` or `components/ui/` folders stay purely technical and primitive—never allowing domain-specific business logic to leak into them.
