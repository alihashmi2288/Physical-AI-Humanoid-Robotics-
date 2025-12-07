# Mobile Responsiveness Architecture

## Component Hierarchy

```
Root
├── Navbar (z-index: 100)
│   ├── Logo
│   ├── Hamburger Menu (mobile only)
│   └── Auth Profile
│
├── PersonalizationBar (z-index: 30)
│   ├── Level Toggle
│   └── Language Toggle
│
├── Main Content
│   ├── Sidebar (desktop: always visible)
│   │   └── Menu Items
│   │
│   └── Doc Content
│       └── Markdown
│
├── Mobile Sidebar (z-index: 200, mobile only)
│   ├── Backdrop (z-index: 199)
│   └── Sidebar Container
│       └── Menu Items
│
├── TextSelectionChat (z-index: 100)
│   ├── Trigger Button
│   └── Modal
│
└── ChatWidget (z-index: 90)
    ├── Toggle Button
    └── Chat Window
```

## Mobile Sidebar Flow

```
User Action: Tap Hamburger Menu
    ↓
JavaScript: Toggle data-hidden attribute
    ↓
CSS: Apply transform: translateX(0)
    ↓
Result: Sidebar slides in from left
    ↓
Backdrop: Appears with opacity transition
    ↓
Body: Scroll prevented
```

## Responsive Breakpoints

```
< 576px: Extra Small Mobile
    - Sidebar width: 85vw
    - Font size: text-xs
    - Padding: p-2

576px - 996px: Mobile/Tablet
    - Sidebar width: 80vw
    - Font size: text-sm
    - Padding: p-3

> 996px: Desktop
    - Sidebar always visible
    - No hamburger menu
    - Full layout
```

## CSS Cascade

```
1. Tailwind Base
2. Tailwind Components
3. Tailwind Utilities
4. custom.css (imported)
5. mobile.css (imported in custom.css)
```

## File Dependencies

```
docusaurus.config.ts
    ↓
src/theme/Root.tsx
    ↓
src/theme/Layout/index.tsx
    ↓
src/css/custom.css
    ↓
src/css/mobile.css
```
