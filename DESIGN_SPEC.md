# Nexus Gaming — Ulwe, Navi Mumbai (nexuscafe.in Design System)

## 1. Canvas & Grid Specifications
* **Reference Website:** [Nexus Gaming (nexuscafe.in)](https://nexuscafe.in/)
* **Target Viewport:** Desktop (1512px $\times$ 982px / 1440px standard)
* **Active Node in Figma:** [Figma Design Canvas (nexuscafe.in Style + Admin Panel Node 17:3)](https://www.figma.com/design/1rfnLNOLZ8x1Q7VembnjuH?node-id=17-3)
* **Base Theme:** Pitch Black Cyber Luxury (`#050505` with subtle CRT scanline effect)

## 2. Typography & Font Pairing (Exact Match)
* **Display / Headings:** **`Space Grotesk`** (Bold / SemiBold — 500, 600, 700)
* **Body & UI Text:** **`DM Sans`** (Regular / Medium / Bold — 400, 500, 600)
* **Technical Metadata & Code Tags:** **`JetBrains Mono`** (`// HARDWARE`, latency `≤ 4 MS`, timestamps)

## 3. Brand Color Palette & Tokens
* **`bg-black`**: `#050505` (Deep pitch black)
* **`bg-card`**: `#0A0A0A` / `#0D0E15`
* **`neon-cyan`**: `#00e5ff` (Primary brand accent, glowing borders, active slots)
* **`cyber-magenta`**: `#d800ff` / `#ff00ff` (Pass redemption, VIP badges)
* **`status-green`**: `#25d366` (Live stations available, WhatsApp status)
* **`border-subtle`**: `rgba(255, 255, 255, 0.1)`

---

## 4. 3-Page Flow Breakdown (nexuscafe.in Style)

### Page 1: Select Battle Station & Time Slots
- **Telemetry Bar:** `OPEN 24/7 · ULWE, NAVI MUMBAI` • `42 STATIONS ONLINE` • `LATENCY: ≤ 4 MS` • `1 GBPS FIBER` • `21°C CLIMATE`.
- **Stations (Exact nexuscafe.in lineup):**
  - **PS5 ELITE LOUNGE (Default Selected @ ₹250/hr):** Sony 4K 120Hz OLED, 1 Remote Included, 50+ Games.
  - **PRO PC STATIONS (₹180/hr):** NVIDIA RTX 5060 Ti, AMD Ryzen 5 7500F, 240Hz 1ms Fast IPS.
  - **PRIVATE SUITES (₹350/hr):** 4-8 Players, Fanatec Direct Drive Sim, 5.1 Surround Theatre.
- **1-Hour Time Slots:** Cyber-styled multi-select slots with `JetBrains Mono` timestamps.
- **Action:** Floating telemetry bar with `NEXT: CONFIGURE GAMES ➔`.

### Page 2: Configure Remotes, Available Games & Cafe Bar
- **Extra Remote Fee:** 1 Player (1 Remote Free) | 2 Players (+₹50) | 3 Players (+₹100) | 4 Players (+₹150).
- **Available Games Library:** High-res game cards for *EA Sports FC 24, Tekken 8, Mortal Kombat 1, Spider-Man 2, It Takes Two, Gran Turismo 7, COD MW3, WWE 2K24*.
- **Personal PSN Account Login:** Option to play using own PlayStation account, cloud saves, and trophies.
- **Cafe Bar Refreshments:** Red Bull (₹125), Monster Energy (₹140), Cold Brew Coffee (₹120), Peri-Peri Fries (₹99).
- **Action:** `PROCEED TO PAYMENT ➔`.

### Page 3: Review, Pass Deduction & UPI Settlement
- **Itemized Invoice:** PS5 Lounge time, extra remote fee, beverages.
- **Pass Rule:** 10-Hour Pass deducts station time (waiving 2h = -₹500). Remote fee (+₹50) and beverages are paid via UPI.
- **UPI QR Code:** Dynamic QR code for ₹50, accepted apps (GPay, PhonePe, Paytm, BHIM), copyable UPI ID (`nexusgaming@okhdfcbank`), and 5-min slot reservation timer.
- **Confirmed Pass Ticket:** Digital pass `#NX-ULWE-8812` ready for reception scan.

---

## 5. Staff & Admin Operations Dashboard

* **Top Telemetry / KPI Cards:**
  - **Today's Revenue:** ₹38,450 (Total UPI & Cash settlements)
  - **Arena Occupancy:** 34 / 42 (81% capacity, 8 free stations)
  - **Pass Hours Redeemed:** 46.0 Hours (across 23 active member passes)
  - **Open Kitchen / Bar Tickets:** 4 pending deliveries
* **Live Arena Station Control (Floor Grid):**
  - Displays live stations: PS5-01, PS5-02, PC-04, VIP-01.
  - Live status: `IN PLAY` (active countdown, gamer name, games preloaded, remotes), `NEXT IN 12M` (ready for checkin), `AVAILABLE`.
  - Actions: `+1H EXTEND`, `CHECK-IN`, `+ ASSIGN`.
* **Transaction Audit Log Table:**
  - Full itemized records: Invoice #, Customer (Google email), Station, Date & Time, Pre-loaded Games, DualSense Remotes, Drinks / F&B items, Paid by Pass? (`YES (-2H / ₹500)` vs `NO`), Final UPI Paid, and `VIEW BILL` action.
* **Live Kitchen Dispense Queue:**
  - Real-time station delivery orders (e.g. `Deliver to PS5-01: 1x Red Bull, 1x Peri-Peri Fries`) with one-click `MARK DELIVERED`.

---

## 6. Official Printable Invoice / Detailed Bill Format
- **Invoice Number:** `#INV-NX-9912`
- **Location & GST:** Plot 14, Sector 19, Ulwe, Navi Mumbai · GSTIN: `27AABCN9912E1Z8`
- **Customer Information:** Name (Deepak Patel), Email, Google SSO Verified status.
- **Station Specs:** Station name (`PS5 ELITE LOUNGE BOOTH 01`), Date (`Saturday, Nov 07, 2026`), Duration & Time (`15:00 - 17:00 (2.0 Hours)`).
- **Games & Account:** Pre-loaded titles (`EA Sports FC 24, Tekken 8`), Login mode (`Cafe Default Profile` or `Personal PSN Account`).
- **Itemized Table:**
  1. Station Hours (2 Hours @ ₹250/hr = ₹500.00)
  2. Extra DualSense Remote (1x Extra = ₹50.00)
  3. Itemized Drinks & Snacks (e.g. Red Bull @ ₹125.00, Peri-Peri Fries @ ₹99.00)
- **Gross Total (Before Pass):** ₹774.00
- **Paid By Pass Status:** `PAID BY PASS: YES (10-HOUR PASS)` $\rightarrow$ Station hours waived (-₹500.00).
- **Net Extras Due:** ₹274.00
- **Final UPI Payment:** `₹274.00 VIA INSTANT UPI` (Txn ID: `UPI/NX/2026/882194` · Status: `SETTLED & CONFIRMED ✓`).



---

## 2. The 3-Page Architecture & Core Business Logic

### Page 1: Station & Time Slots Selection
- **SSO Header:** User avatar, name, email, and active 10-Hour Pass pill (`🎟️ 10-Hr Pass: 4h left`).
- **Device Selection:**
  - **Default Selected: PlayStation 5 Lounge (₹250/hr)**.
  - PC Esports Rig (₹180/hr) & Racing Simulator Cockpit (₹350/hr).
- **Time Slots:** 1-hour minimum blocks with multi-select support (e.g. 3:00 PM – 5:00 PM = 2 hours).
- **Bottom Summary Bar:** Shows rig name, hours picked, and button `Next: Choose Games & Add-ons ➔`.

### Page 2: Customization, Games & Add-ons (The Cart Page)
- **Guest / Player Remote Logic:**
  - Base PS5 rental includes: **1 DualSense Remote (Free)**.
  - 1 Player: 1 Remote (+₹0).
  - 2 Players: 2 Remotes (+1 Extra Remote = **+₹50**).
  - 3 Players: 3 Remotes (+2 Extra Remotes = **+₹100**).
  - 4 Players: 4 Remotes (+3 Extra Remotes = **+₹150**).
- **Available Games Catalog:**
  - Pre-loaded titles: *EA Sports FC 24*, *Tekken 8*, *Mortal Kombat 1*, *Marvel's Spider-Man 2*, *It Takes Two*, *Gran Turismo 7*, *Call of Duty: MW3*, *WWE 2K24*.
  - User can toggle and select the games they want pre-updated for their session.
- **Personal Game Login Toggle:**
  - Option: *"🔑 Log in with Personal PSN Account (Play cloud saves, own digital library & earn personal trophies)"*.
- **Beverages & Snacks (Pre-Order or On-Demand):**
  - Items: Red Bull (₹125), Monster Energy Ultra (₹140), Iced Hazelnut Cold Coffee (₹120), Peri-Peri Fries (₹99).
  - Note: Chilled and delivered to station on arrival, or available to order on-demand from seat.
- **Bottom Summary Bar:** Updates total (Time + Remote + Snacks) $\rightarrow$ `Proceed to Payment ➔`.

### Page 3: Review, Pass Redemption & UPI Payment
- **Itemized Bill:**
  - PS5 Rig (2 Hours @ ₹250/hr) = ₹500
  - Extra DualSense Remote (1x) = ₹50
  - Beverages & Snacks = ₹XX
- **Pass Deduction Business Rule:**
  - When user applies their **10-Hour Pass**, it **reduces the station time cost** (-₹500 / 2 hours deducted).
  - It does **NOT** reduce additional charges (extra remote charge ₹50 + beverages).
  - **UPI Due:** Exactly ₹50 (or ₹50 + snacks).
- **Instant UPI QR & Deep Links:**
  - Dynamic QR code pre-filled with the exact net payable amount.
  - Authentic badges for Google Pay, PhonePe, Paytm, and BHIM.
  - Copyable UPI VPA (`nexuscafe@okhdfcbank`) and 5-minute reservation hold timer.
- **Confirmation Ticket:** Shows digital ticket pass `#NX-PS5-7721` with confirmed games, controller count, and pass balance.


---

## 2. Color Palette & Design Tokens

| Token Name | Hex Code | Usage |
| :--- | :--- | :--- |
| **`bg-canvas`** | `#08090E` | Deep obsidian background |
| **`bg-card`** | `#12141F` | Elevated card surfaces (PC, Sim, Slots) |
| **`bg-card-active`** | `#13172E` | Hero card surface (PlayStation 5 selected state) |
| **`border-subtle`** | `rgba(255, 255, 255, 0.05)` | Card boundaries, dividers |
| **`ps-blue`** | `#0070D1` | PlayStation branding, primary buttons, active slot border |
| **`neon-cyan`** | `#00F0FF` | Accents, highlights, step badges, pricing highlights |
| **`emerald-ready`** | `#10B981` | "Open Now", "3 Booths Ready", available indicators |
| **`purple-pass`** | `#8B5CF6` | 10-Hour Gamer Pass badge, pass redemption toggle |
| **`red-soldout`** | `#EF4444` | Booked / Sold-out slots |

---

## 3. Typography Hierarchy
* **Headings & Badges:** `Space Grotesk` (Bold / SemiBold) — modern geometric tech feel.
* **Body, UI & Numbers:** `Plus Jakarta Sans` (400, 500, 600, 700) — high legibility on dark displays.

---

## 4. UI Section Breakdown

### A. Top Sticky Header (Height: 64px)
```
[ 🎮 APEX GAME LOUNGE (Open Now • 10AM-11PM) ]       [ Today, Nov 7 | Tomorrow | Sat ]       [ 🎟️ 10-Hr Pass (4h left) ] [ 👤 Deepak Patel ▾ ]
```
1. **Brand Lockup (Left):**
   - Glowing gradient logo icon (Blue to Cyan).
   - "APEX GAME LOUNGE" typography with live status indicator (pulsing green dot).
2. **Date Quick-Switch (Center):**
   - Segmented control pills: `Today, Nov 7` (Active), `Tomorrow, Nov 8`, `Saturday, Nov 9`.
3. **User Profile & SSO (Right):**
   - Active Pass Indicator: Shows hours remaining without needing to click into settings.
   - Google Profile Pill: High-res Google Avatar, Name, Email, and quick dropdown for "My Bookings" and "Sign Out".

---

### B. Device Showcase Ribbon (Middle)
```
+--------------------------------------+  +---------------------------+  +---------------------------+
| ★ DEFAULT SELECTED                   |  |                           |  |                           |
| [PS5 Icon]              ₹250 / hr    |  | [PC Icon]      ₹180 / hr  |  | [Wheel Icon]    ₹350 / hr |
| PlayStation 5 Lounge    3 Booths Ready| | PC Gaming Rig   6 Rigs Ready| | Racing Sim      1 Rig Left|
| 55" 4K OLED • Couch • 1-4 Controllers|  | RTX 4070 • 240Hz 1ms IPS  |  | Fanatec Wheel • Cockpit   |
| [FC 24] [Tekken 8] [MK 1] [Spider-Man]  | [Valorant] [CS2] [Apex]   |  | [F1 24] [Assetto Corsa]   |
+--------------------------------------+  +---------------------------+  +---------------------------+
```
* **PS5 Lounge Card (Default State):**
  * Border: `border-2 border-blue-500` with soft blue glow (`box-shadow: 0 0 25px rgba(0, 112, 209, 0.4)`).
  * Prominent "Default Selected" badge in top right corner.
  * Instant game tags so customers know what's ready to play.

---

### C. Available Time Slots Grid (1-Hour Blocks)
```
11:00 AM - 12:00 PM    12:00 PM - 01:00 PM    01:00 PM - 02:00 PM    02:00 PM - 03:00 PM
[ Available • ₹250 ]    [ Available • ₹250 ]    [ 🔒 Sold Out ]        [ Available • ₹250 ]

03:00 PM - 04:00 PM    04:00 PM - 05:00 PM    05:00 PM - 06:00 PM    06:00 PM - 07:00 PM
[ ✓ SELECTED ]         [ ✓ SELECTED ]         [ Available • ₹250 ]    [ ⚡ 1 Rig Left ]
```
* **Slot Dimensions:** Height: 96px, rounded-xl (`12px`).
* **Multi-Select Behavior:** Clicking any available slot toggles selection. Selected slots illuminate in solid PlayStation Blue with a checkmark.
* **Pricing feedback:** Real-time unit price shown on each slot card.

---

### D. Floating Bottom Action Bar (Checkout Trigger)
```
[ ⏱️ PS5 Lounge • 2 Hours (3:00 PM - 5:00 PM) ]                   [ Total: ₹500 ]  [ Proceed to Checkout ➔ ]
```
* Anchored to bottom of the viewport with backdrop-blur (`rgba(15, 17, 29, 0.95)`).
* Slides up smoothly when $\ge 1$ slot is selected; auto-hides if all slots are deselected.

---

### E. Checkout Modal & UPI Payment Pipeline
1. **Summary:** Device, date, consecutive time block (e.g. 3:00 PM – 5:00 PM).
2. **Guest / Controller Selector:**
   * 4-option segment: `1 Solo` | `2 Duo (Default)` | `3 Players` | `4 Squad`.
   * Helper note: *"2 DualSense controllers will be sanitized and connected for your arrival."*
3. **Pass Redemption:**
   * 1-click toggle: *"Redeem 2 hours from your 10-Hour Pass"*.
   * Immediately zeroes out the payable amount.
4. **Dynamic UPI Payment:**
   * Dynamic QR Code pre-filled with transaction payload (`upi://pay?pa=apexgamecafe@okhdfcbank&pn=ApexGameLounge&am=500&cu=INR`).
   * Supported UPI app icons: Google Pay, PhonePe, Paytm, BHIM.
   * Direct copyable UPI ID + 5-minute countdown reservation lock timer.
