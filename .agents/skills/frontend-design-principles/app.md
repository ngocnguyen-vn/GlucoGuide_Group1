# Application UI Design Principles (`app.md`)

Use this guide when building or reviewing product interfaces: dashboards, admin and settings panels, internal tools, SaaS software, and data-heavy surfaces (tables, forms, complex lists) where users spend extended periods working repeatedly.

---

## 1. Ergonomics for Repeated Use

- **Utility over spectacle:** Marketing persuades in 5 seconds; software serves for 8 hours a day. Favor visual calm, ergonomic predictability, and fast information scanning over visual novelty.
- **Visual hierarchy that whispers:** Don't shout with contrasting boxes. Use muted structural lines, subtle background shifts, and restrained font weights.
- **Density is a feature, not a bug:** Professional users need information density. Do not pad everything with 24px of whitespace if it forces unnecessary scrolling. Keep data compact and legible.

---

## 2. Navigation & Wayfinding

- **Navigation IS the product architecture:** The user must instantly know:
  1. *Where am I right now?*
  2. *What can I act on immediately?*
  3. *How do I get back?*
- **Persistent orientation:** Always provide clear active states in sidebars or top bars, breadcrumbs for deep hierarchies, and sensible page headers.
- **Keyboard navigation & command bars:** Power users expect quick shortcuts (`Cmd/Ctrl+K`), tab-order sanity, and focused form interaction.

---

## 3. Data Representation: Tables, Lists & Metrics

- **Tables:**
  - Right-align numbers and currencies.
  - Left-align textual content.
  - Center status badges or icons when necessary.
  - Keep headers subtle: uppercase 11-12px with tracked-out spacing (`letter-spacing: 0.05em`) and subdued text color.
  - Hover states on rows should be whisper-quiet (e.g. background brightness change of 2-3%).
- **Metrics & KPIs:**
  - Avoid identical "icon on left, big number, label on top" cards everywhere.
  - Select representation based on context: sparklines for trend over time, comparison deltas (+12% vs last month), progress bars for quotas, or clean singular callouts.
- **Empty & Loading States:**
  - Skeletons should mirror actual content layout, not generic flashing gray blocks.
  - Empty states should offer a clear next action or explanation, not dead ends.

---

## 4. Forms & Interactive Controls

- **Input Fields:**
  - Consistent vertical cadence (label $\rightarrow$ input $\rightarrow$ helper text/error).
  - Clear, accessible focus rings that don't obscure adjacent elements.
  - Group related fields logically; don't stretch single text inputs across 100% of an ultrawide monitor.
- **Action Buttons:**
  - One primary action per view or form block.
  - Destructive actions separated or requiring deliberate confirmation.
  - Inline feedback on asynchronous operations (saving indicators, disable-on-submit).

---

## 5. Token System for Applications

Use semantic, functional tokens rather than generic color steps:

```css
:root {
  /* Surfaces */
  --app-bg: #f8fafc;
  --surface-canvas: #ffffff;
  --surface-raised: #f1f5f9;
  --surface-overlay: #ffffff;
  
  /* Borders */
  --border-subtle: rgba(0, 0, 0, 0.06);
  --border-strong: rgba(0, 0, 0, 0.12);
  
  /* Text */
  --text-primary: #0f172a;
  --text-secondary: #64748b;
  --text-muted: #94a3b8;
  
  /* Domain Accent */
  --accent-primary: ...;
  --accent-subtle: ...;
}
```
