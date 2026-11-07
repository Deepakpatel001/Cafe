# Nexus Gaming — Project Implementation Plan

## 1. Project Overview & Scope

Nexus Gaming is a luxury gaming cafe web platform modeled after the brand identity and operational standards of **[nexuscafe.in](https://nexuscafe.in/)** (Ulwe, Navi Mumbai). The platform unifies:
- **Gamer 3-Page Booking Portal:**
  1. *Station & 1-Hour Time Slots Selection* (Default: PS5 Elite Lounge).
  2. *Customization & Cart* (Pre-loaded games, personal PSN login toggle, extra DualSense remote fees, and chilled beverages/snacks).
  3. *Review, Pass Deduction & Instant UPI Settlement* (Pass covers station time only; extra remotes and food are paid via UPI).
- **Staff & Admin Operations Dashboard:**
  - Real-time station telemetry & occupancy tracking (42 stations).
  - Live floor control (active session timers, remote prep, manual walk-in assignments, +1h extensions).
  - Transaction audit log & full printable tax invoices (`#INV-NX-...`).
  - Live Kitchen / Bar dispense queue for in-seat delivery.

---

## 2. Monorepo Architecture & Directory Layout

```text
Cafe/
├── docker-compose.yml              # Local MongoDB & Redis infrastructure
├── docs/                           # Figma references and design specifications
├── packages/
│   └── shared/                     # Shared TypeScript types, Zod schemas, API clients
├── apps/
│   ├── web/                        # React (Vite) + Tailwind CSS (Space Grotesk, DM Sans, JetBrains Mono)
│   └── mobile/                     # React Native (Expo) - Planned Android App
└── services/                       # Python FastAPI Microservices
    ├── auth-service/               # Google SSO verification, JWT issuance (:8001)
    ├── booking-service/            # Station inventory, 1h slot engine, Redis distributed lock (:8002)
    ├── billing-service/            # 10-Hour Pass deduction & UPI invoice calculator (:8003)
    └── order-service/              # Cafe bar menu, in-seat cart, KDS queue (:8004)
```

---

## 3. Phased Rollout Roadmap

### Phase 1: Infrastructure & Data Foundations (Week 1)
- [ ] **Task 1.1:** Setup `docker-compose.yml` with MongoDB 7.0 and Redis 7.0 (with persistent volumes and health checks).
- [ ] **Task 1.2:** Initialize Python virtual environment and shared FastAPI core library (Pydantic models, MongoDB Motor async client, Redis connection pool).
- [ ] **Task 1.3:** Seed initial station hardware specs (PS5 Elite Lounges, Pro PC RTX 5060 Ti rigs, Private VIP Suites) and cafe refreshments menu.

### Phase 2: Core Microservices & Business Logic (Weeks 2–3)
- [ ] **Task 2.1: Auth Service (`:8001`)**
  - Implement Google SSO ID token verification endpoint (`POST /auth/google`).
  - Issue stateless JWT Bearer tokens with user roles (`GAMER`, `STAFF`, `ADMIN`).
- [ ] **Task 2.2: Booking & Slot Service (`:8002`)**
  - Implement 1-hour time slot generator across operating hours (10:00 AM – 11:30 PM).
  - Implement Redis atomic slot locking (`SET lock:station:{id}:{slot} NX EX 300`) to hold seats during checkout.
- [ ] **Task 2.3: Billing & Pass Service (`:8003`)**
  - Implement 10-Hour Pass balance tracker.
  - Implement the **Exact Pass Deduction Rule**: Pass waives station time hours only; extra remote fees (+₹50 each) and refreshments remain payable via UPI.
  - Generate dynamic UPI payment deep links (`upi://pay?...`) and QR payloads.
- [ ] **Task 2.4: Order & KDS Service (`:8004`)**
  - Food & beverage catalog endpoints.
  - Real-time station delivery ticket pipeline (`PENDING` $\rightarrow$ `PREPARING` $\rightarrow$ `DELIVERED`).

### Phase 3: React Frontend Portal (`apps/web`) (Weeks 4–5)
- [ ] **Task 3.1:** Setup Vite + React 19 + Tailwind CSS configured with exact `nexuscafe.in` design tokens (`#050505` pitch black, `#00e5ff` cyan, `#d800ff` magenta, `#25d366` green, scanline overlay).
- [ ] **Task 3.2:** Build **Page 1: Rig & Slot Picker**:
  - Telemetry top strip (`OPEN 24/7 · ULWE`, `≤ 4 MS`).
  - PS5 Elite Lounge default selected card + Pro PC & VIP Suite options.
  - 1-hour slot multi-selector with real-time floating action bar.
- [ ] **Task 3.3:** Build **Page 2: Games, Remotes & Cart**:
  - Available PS5 games grid (EA FC 24, Tekken 8, MK 1, Spider-Man 2, etc.).
  - Personal PSN Account login toggle.
  - DualSense controller counter (1 included free, +₹50 per extra remote).
  - Refreshments pre-order section.
- [ ] **Task 3.4:** Build **Page 3: Invoice & Instant UPI Payment**:
  - Pass redemption toggle with itemized discount calculation.
  - Dynamic UPI QR code with GPay, PhonePe, Paytm, BHIM badges.
  - Copyable UPI VPA + 5-minute countdown reservation timer.
- [ ] **Task 3.5:** Build **Printable Detailed Invoice Modal**:
  - Complete tax receipt with GSTIN, date, time, games, remotes, drinks, and pass waiver line item.

### Phase 4: Staff & Admin Operations Dashboard (Week 6)
- [ ] **Task 4.1:** Build Top KPI telemetry cards (Today's Revenue, Arena Occupancy 34/42, Pass Hours Redeemed, Open F&B Tickets).
- [ ] **Task 4.2:** Build Live Arena Floor Grid with station status indicators, active countdown timers, and quick actions (`+1H EXTEND`, `CHECK-IN`, `+ ASSIGN`).
- [ ] **Task 4.3:** Build Transaction Audit Log Table with search, status filters, and instant `VIEW BILL` modal preview.
- [ ] **Task 4.4:** Build Live Station F&B Delivery Queue with `MARK DELIVERED ✓` action for kitchen/bar staff.

### Phase 5: Verification, Testing & Production Hardening (Week 7)
- [ ] **Task 5.1:** Automated Unit and Integration tests using `pytest` and `pytest-asyncio`.
- [ ] **Task 5.2:** Concurrency testing on Redis slot locking (ensuring 0% double booking rate under heavy load).
- [ ] **Task 5.3:** End-to-end Cypress / Playwright test walking through the 3-step customer booking and admin reflection.

### Phase 6: Mobile Android App Preparation (Week 8+)
- [ ] **Task 6.1:** Bootstrap `apps/mobile` with React Native (Expo).
- [ ] **Task 6.2:** Import shared API clients and Zustand stores from `packages/shared`.
- [ ] **Task 6.3:** Integrate `expo-camera` for in-cafe rig QR scanning and persistent countdown lock-screen notifications.

---

## 4. Key Milestones & Acceptance Criteria

| Milestone | Deliverables | Acceptance Criteria |
| :--- | :--- | :--- |
| **M1: Core Booking Engine** | `booking-service` + Redis Lock | Slot locking works with 5-minute TTL; simultaneous attempts on the same rig slot return conflict. |
| **M2: Billing & Pass System** | `billing-service` + UPI QR | Pass deduction reduces station hours to ₹0; extra remotes & drinks remain payable; UPI QR generates correct sum. |
| **M3: 3-Page Gamer Webapp** | `apps/web` (Pages 1, 2, 3) | Matches Figma node `17:3` design; user can pick PS5, select 2 hours, pick games, add remote & drink, and pay via UPI. |
| **M4: Admin Dashboard** | Admin Portal & KDS | Real-time floor statuses update; staff can view detailed bill and mark drinks delivered. |
| **M5: Full System Integration** | Dockerized Monorepo | Entire platform spins up with `docker-compose up` with zero manual configuration. |

---

## 5. Risk Management & Edge Cases

1. **Simultaneous Booking Collisions:**
   * *Mitigation:* Handled via Redis `SET ... NX EX 300` distributed locking at the database level before payment initiation.
2. **Payment Timeout / Abandonment:**
   * *Mitigation:* If UPI payment is not confirmed within 5 minutes, Redis TTL expires and frees the slot automatically.
3. **Pass Hours Exhaustion Mid-Booking:**
   * *Mitigation:* System validates remaining pass hours; if user has only 1 hour left on pass but books 2 hours, the pass covers 1 hour (-₹250) and remaining 1 hour (+₹250) is automatically routed to UPI payment.
4. **Offline / Network Latency in Cafe:**
   * *Mitigation:* Client-side optimistic timers with server timestamp synchronization.
