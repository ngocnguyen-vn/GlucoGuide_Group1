# Technical Design Foundations (`references/principles.md`)

Concrete implementation details, CSS variables, and structural systems for spacing, depth, typography, colors, and dark mode.

---

## 1. Spacing System

Enforce a strict spatial scale based on a 4px/8px rhythm. Never use arbitrary pixel numbers.

```css
:root {
  --space-1: 4px;   /* Tight element gaps, icon offsets */
  --space-2: 8px;   /* Badge padding, list item gaps */
  --space-3: 12px;  /* Compact card padding, button gaps */
  --space-4: 16px;  /* Standard input padding, card inner margins */
  --space-6: 24px;  /* Section gutters, component container padding */
  --space-8: 32px;  /* Major block separation */
  --space-12: 48px; /* Layout grid breaks, hero padding */
  --space-16: 64px; /* Macro section spacing */
}
```

### Rules:
- **Proximity:** Elements that belong together must be grouped closer than unrelated items.
- **Symmetry:** Margins and paddings should be symmetrical unless intentionally offset for alignment.

---

## 2. Depth & Layering System

Never mix depth strategies randomly. Prefer subtle borders or whisper-quiet elevation shifts over dramatic dark drop shadows.

```css
:root {
  /* Quiet elevation system */
  --elevation-flat: none;
  --elevation-low: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
  --elevation-mid: 0 4px 6px -1px rgba(0, 0, 0, 0.07), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
  --elevation-high: 0 10px 15px -3px rgba(0, 0, 0, 0.08), 0 4px 6px -4px rgba(0, 0, 0, 0.04);
  
  /* Borders for structure */
  --border-hairline: 1px solid var(--border-color);
}
```

### Depth Rules:
- **Whisper-quiet:** If the border or shadow is the first thing a user sees, it is too heavy.
- **Single Strategy:** Use either crisp borders with hairline dividers OR soft elevations. Don't layer heavy borders onto heavy shadows.

---

## 3. Typography Scale & Implementation

Typography is not just a container for copy; it defines the emotional temperature and functional clarity.

```css
:root {
  /* Font Families */
  --font-sans: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  --font-mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;

  /* Type Scale */
  --text-xs: 0.75rem;    /* 12px - Labels, tags, timestamps */
  --text-sm: 0.875rem;   /* 14px - Table data, secondary copy, controls */
  --text-base: 1rem;     /* 16px - Body text */
  --text-lg: 1.125rem;   /* 18px - Subheadings, card titles */
  --text-xl: 1.25rem;    /* 20px - Section headings */
  --text-2xl: 1.5rem;    /* 24px - Page titles */
  --text-3xl: 1.875rem;  /* 30px - Hero / display headers */

  /* Line Heights */
  --leading-none: 1;
  --leading-tight: 1.25;
  --leading-snug: 1.375;
  --leading-normal: 1.5;
  --leading-relaxed: 1.625;
}
```

### Type Rules:
- **Uppercase Labels:** Always add tracking (`letter-spacing: 0.05em` to `0.08em`) when using uppercase text under 14px.
- **Reading Measure:** Restrict paragraph containers to 45–75 characters per line (`max-width: 65ch`).

---

## 4. Color System & Token Naming

Name tokens by their domain and semantic role, not their literal color code:

```css
/* Light Mode */
:root {
  --canvas-bg: #fafafa;
  --surface-default: #ffffff;
  --surface-subtle: #f4f4f5;
  
  --border-default: #e4e4e7;
  --border-subtle: #f4f4f5;
  
  --text-primary: #18181b;
  --text-secondary: #71717a;
  --text-muted: #a1a1aa;
}

/* Dark Mode */
[data-theme="dark"] {
  --canvas-bg: #09090b;
  --surface-default: #121215;
  --surface-subtle: #1c1c20;
  
  --border-default: #27272a;
  --border-subtle: #1e1e22;
  
  --text-primary: #f4f4f5;
  --text-secondary: #a1a1aa;
  --text-muted: #71717a;
}
```

### Dark Mode Principles:
- **Never pure #000000:** Pitch black canvas causes harsh visual strain; use very deep tinted grays (e.g. `#09090b` or `#0b0f19`).
- **Elevation via lightness:** In dark mode, shadows disappear. Simulate elevation by making higher surfaces slightly lighter in tone or applying subtle luminous borders.
