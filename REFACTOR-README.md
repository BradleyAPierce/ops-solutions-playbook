# Ops Solutions Playbook - Refactored Structure

This WordPress site has been refactored into a static site with centralized assets and reusable components.

## 📁 Folder Structure

```
ops-solutions-playbook/
├── assets/                          # GLOBAL assets for all 40 pages
│   ├── css/
│   │   ├── vendor/                  # Third-party CSS (Bootstrap, plugins, etc.)
│   │   └── core/
│   │       └── wordpress-extracted.css  # All WordPress inline CSS extracted
│   ├── js/
│   │   ├── vendor/                  # Third-party JS (jQuery, Bootstrap, etc.)
│   │   ├── modules/                 # Feature-specific modules
│   │   └── component-loader.js      # Loads header/nav/footer into pages
│   └── images/
│       ├── logos/                   # Logo files
│       ├── icons/                   # Favicon and icons
│       └── content/                 # Content images
├── components/                      # GLOBAL components used by all pages
│   ├── header.html                  # Site header (logo, search)
│   ├── nav.html                     # Main navigation menu
│   └── footer.html                  # Site footer
├── pages/
│   └── index.html                   # ✅ REFACTORED TEMPLATE
└── index/
    └── index.html                   # ❌ OLD WordPress export (DO NOT USE)
```

## ✅ What Was Done (One-Shot Refactor)

### 1. **Asset Organization**

- ✅ Moved all CSS from `/index/index_files/` → `/assets/css/vendor/`
- ✅ Moved all JS from `/index/index_files/` → `/assets/js/vendor/`
- ✅ Moved all images → `/assets/images/` (organized by type)

### 2. **Inline Code Extraction**

- ✅ Extracted all WordPress inline `<style>` tags → `/assets/css/core/wordpress-extracted.css`
- ✅ Created modular component structure with header/nav/footer
- ✅ Created component loader JavaScript

### 3. **Google Tag Manager Removal**

- ✅ All GTM tracking code removed
- ✅ No analytics/tracking scripts present

### 4. **Component System**

- ✅ Created `/components/header.html` - Reusable header
- ✅ Created `/components/nav.html` - Reusable navigation menu
- ✅ Created `/components/footer.html` - Reusable footer
- ✅ Created `/assets/js/component-loader.js` - Dynamically injects components

## 🎯 How to Use This for All 40 Pages

### Step 1: Copy the Template

Use `/pages/index.html` as your template for ALL pages:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <!-- Global CSS - same for all pages -->
    <link rel="stylesheet" href="/assets/css/vendor/bootstrap.min.css" />
    <link rel="stylesheet" href="/assets/css/vendor/plugin.css" />
    <link rel="stylesheet" href="/assets/css/vendor/utilities.css" />
    <link rel="stylesheet" href="/assets/css/vendor/vendor.css" />
    <link rel="stylesheet" href="/assets/css/vendor/style.css" />
    <link rel="stylesheet" href="/assets/css/core/wordpress-extracted.css" />
  </head>
  <body>
    <!-- Global components - loaded via JS -->
    <div id="header-container"></div>
    <div id="nav-container"></div>

    <!-- PAGE-SPECIFIC CONTENT GOES HERE -->
    <main>...your unique page content...</main>

    <!-- Global footer -->
    <div id="footer-container"></div>

    <!-- Global JS - same for all pages -->
    <script src="/assets/js/vendor/jquery.min.js"></script>
    <script src="/assets/js/vendor/bootstrap.min.js"></script>
    <script src="/assets/js/component-loader.js"></script>
  </body>
</html>
```

### Step 2: Extract Page Content

For each of your 40 WordPress exports:

1. Open the exported HTML
2. Find the `<main>` content (between header and footer)
3. Copy only that content
4. Paste into the template where it says "PAGE-SPECIFIC CONTENT GOES HERE"
5. Update image URLs to point to `/assets/images/`

### Step 3: Update Image Paths

Replace WordPress CDN URLs with local paths:

```html
<!-- OLD -->
<img src="https://solutionsmkm.b-cdn.net/wp-content/uploads/2019/03/logo.svg" />

<!-- NEW -->
<img src="/assets/images/logos/logo.svg" />
```

## 🚀 Running the Site

### Option A: Local Web Server (Recommended)

Components are loaded via `fetch()`, which requires a web server:

```bash
# Using Python 3
cd /Users/bradleypierce/Developer/ops-solutions-playbook
python3 -m http.server 8000

# Using Node.js
npx http-server -p 8000

# Using PHP
php -S localhost:8000
```

Then open: `http://localhost:8000/pages/index.html`

### Option B: VS Code Live Server

1. Install "Live Server" extension
2. Right-click on `/pages/index.html`
3. Select "Open with Live Server"

## 🎨 Customizing Headers Per Page

The component loader supports **data attributes** for per-page header customization:

### Custom Logo

```html
<!-- Default header (uses logo from components/header.html) -->
<div id="header-container"></div>

<!-- Custom logo for this page only -->
<div
  id="header-container"
  data-logo="/assets/images/logos/healthcare-logo.svg"></div>
```

### Custom Subtitle

```html
<!-- Custom subtitle image -->
<div
  id="header-container"
  data-subtitle="/assets/images/content/custom-subtitle.svg"></div>
```

### Both Logo + Subtitle

```html
<!-- Customize both -->
<div
  id="header-container"
  data-logo="/assets/images/logos/finance-logo.svg"
  data-subtitle="/assets/images/content/finance-subtitle.svg"></div>
```

The component loader automatically applies these attributes after loading the header HTML.

## 🔄 Asset Deduplication Process

When refactoring the remaining 39 pages, **I will automatically prevent asset duplication**:

### What I Check

- ✅ **CSS files**: Compare filenames and checksums before copying
- ✅ **JS files**: Skip if already in `/assets/js/vendor/`
- ✅ **Images**: Check for duplicates in `/assets/images/` before adding
- ✅ **Inline CSS**: Only extract unique styles not already in `wordpress-extracted.css`

### What This Means

- 📁 **No bloat**: Most pages use the same Bootstrap, jQuery, theme CSS
- 💾 **Smaller repo**: Shared assets referenced 40x instead of copied 40x
- ⚡ **Faster updates**: Change one file → affects all pages
- 🧹 **Clean structure**: `/assets/` stays organized with only unique files

### Example

```
Page 1: Uses bootstrap.min.css → Copied to /assets/css/vendor/
Page 2: Uses bootstrap.min.css → ✓ Already exists, skip copy
Page 3: Uses bootstrap.min.css → ✓ Already exists, skip copy
...
Page 40: Uses bootstrap.min.css → ✓ Already exists, skip copy

Result: ONE file shared by all pages instead of 40 copies
```

## 📝 Next Steps

1. **Test the template**: Open `/pages/index.html` in a browser with a local server
2. **Apply to all 40 pages**: Use the template structure for each page
3. **Update navigation**: Modify `/components/nav.html` if menu links need adjustment
4. **Customize styling**: Edit `/assets/css/core/` files as needed

## ⚠️ Important Notes

- **DO NOT edit** `/index/index.html` - this is the old WordPress export
- **USE** `/pages/index.html` - this is the new refactored template
- All pages should import from `/assets/` and `/components/` at the root
- No duplication needed - one set of assets serves all 40 pages
- Components are loaded client-side via JavaScript

## 🔍 File Reference

- **Template**: `/pages/index.html`
- **Global Header**: `/components/header.html`
- **Global Nav**: `/components/nav.html`
- **Global Footer**: `/components/footer.html`
- **Component Loader**: `/assets/js/component-loader.js`
- **Extracted CSS**: `/assets/css/core/wordpress-extracted.css`
