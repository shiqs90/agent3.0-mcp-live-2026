# 🤖 Class 11 — Agents, Middleware & Memory: Giving CineBot a Mind
### Agentic AI 3.0 Specialization | Live Class 2026

**🎙️ Mentor:** Mayank Aggarwal · **📅 Date:** 1 August 2026 · **⏱️ Duration:** ~4.5 hours

> 📂 **Code for this class:** [`11-12 - 1-8 Aug - Agents, Memory & Middleware/`](<../11-12 - 1-8 Aug - Agents, Memory & Middleware/>) — [`Agent-Middleware-Architecture.excalidraw`](<../11-12 - 1-8 Aug - Agents, Memory & Middleware/Agent-Middleware-Architecture.excalidraw>) · [`MIddleware.ipynb`](<../11-12 - 1-8 Aug - Agents, Memory & Middleware/MIddleware.ipynb>)

---

## 🧠 Everything So Far Was Already "Agents"

> *"What has actually changed over the last 4–5 years? We've just bought an artificial brain. Apart from the LLM, everything else is the same. The whole idea becomes: how do we best harness this model?"*

Models, messages, structured output, and tools were never separate topics from agents — they're the components an agent is built from.

## ⚖️ Not Every Tool Belongs to Every User

A booking agent has a standard tool, a VIP-lounge tool, and an admin tool. Asking the user "are you a VIP?" doesn't work (everyone says yes); silently removing the tool breaks it for real VIPs.

> *"A menu that reprints itself before you sit down. A VIP member sees the full menu — not because they were told 'don't order the VIP item,' but because it isn't printed on their menu at all."*

## 🎛️ Dynamic Tool Loading via Middleware

```mermaid
flowchart LR
    A["📨 Request"] --> M1["🧵 before model"]
    M1 --> B["🧠 Model call"]
    B --> M2["🧵 after model"]
    M2 --> C["🛠️ Tool call"]

    style M1 fill:#f59e0b,color:#fff
    style M2 fill:#f59e0b,color:#fff
```

```python
def vip_gate_middleware(request):
    is_vip = request.state.get("is_vip_member", False)
    if not is_vip:
        request.tools = [t for t in request.tools if t.name != "vip_lounge_booking"]
    return request
```

Plain Python `if`/`else` outside the agent can't see the agent's own live state — reading `state` at runtime is only possible from inside the agent's execution, which middleware provides. Getting this to actually read a passed-in flag correctly required defining a **custom state schema** telling the agent to track `is_vip_member` explicitly, alongside its built-in message list.

## 🖐️ Headless Tools

Tools whose *implementation* runs on the **user's own device** — clipboard, geolocation, payment — not the server. Definitions are registered with the agent; execution happens client-side after an interrupt/resume handshake. Same idea as browser geolocation/clipboard APIs, just triggered by an agent.

## 🧳 TripMate — Real Tools, Not Mocks

A second project introduced alongside CineBot: real weather via **Open-Meteo** (free, keyless), real search via **Tavily**, and a real **SQLite** table for saving/retrieving trips — so the project survives an application restart, unlike anything held only in memory.

## 🕳️ The Forgetting Problem → Checkpointing

```python
from langgraph.checkpoint.memory import InMemorySaver

checkpointer = InMemorySaver()
agent_with_memory = create_agent(model=model, tools=[...], checkpointer=checkpointer)

config = {"configurable": {"thread_id": "mayank-session-1"}}
agent_with_memory.invoke({"messages": [...]}, config=config)
```

`thread_id` is just a unique key the checkpointer uses to locate a conversation — the application controls it, the user never sees it directly.

| Concept | For | Lifetime |
|---|---|---|
| **Memory saver** (checkpointer) | One conversation's history, tied to `thread_id` | Minutes to persistent |
| **Memory store** | Facts *about a user*, usable across conversations | Persistent by design |
| **Caching** | Avoiding repeated expensive calls | Short, tunable |
| **Database** | General persistent app storage | Persistent |

## ✅ Action Items

- [ ] 🔁 Recreate the VIP middleware example, including the state-schema bug and its fix
- [ ] 🧵 Write middleware that filters tools based on `request.state`
- [ ] 🌦️ Build one genuinely real tool (free public API, no key)
- [ ] 🗄️ Confirm `InMemorySaver` + `thread_id` remembers across two `invoke()` calls, then forgets on a new `thread_id`

---

## ➡️ Up Next
**[Class 12 — 8 Aug — Mastering Middleware: Control, Guardrails & HITL »](<12 - 08 Aug - Mastering Middleware.md>)**

---
*Part of the [Live-Class-2026](../README.md) class summary index. ⬅️ [Class 10](<10 - 26 Jul - Tools Deep Dive.md>)*
