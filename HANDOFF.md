# HANDOFF DOCUMENT - WordPress to Static Site Refactoring

**Last Updated:** February 5, 2026  
**Progress:** 22/~40 pages (55% complete)  
**Context:** Mid-refactoring handoff for new chat session

---

## 🎯 PROJECT OVERVIEW

### What We're Doing

Refactoring ~40 WordPress-exported HTML pages into a clean static site with:

- **Centralized assets** at `/assets/` (CSS, JS, images)
- **Reusable components** at `/components/` (header, nav, footer)
- **Component loader** system (client-side JavaScript injection)
- **No duplication** - one set of assets serves all pages

### Why This Matters

- **Before:** 3,000+ line files with massive inline CSS/JS
- **After:** ~200-300 line clean HTML files
- **Benefit:** 85%+ reduction in code, easier maintenance

---

## ✅ COMPLETED WORK (22 pages = 55%)

### Refactored Sections:

1. **Core/Cloud** (7 pages) ✅
   - Location: `/pages/core/cloud/`
   - device-management, document-management, fax-solutions, intelligent-document-processing, konica-minolta-marketplace, print-management, security

2. **Core/On-Premises** (7 pages) ✅
   - Location: `/pages/core/on-premises/`
   - device-management, integrated-option-solutions, intelligent-document-processing, mobile-applications, pdf-editing, print-management, security

3. **Vertical** (4 pages) ✅
   - Location: `/pages/vertical/`
   - finance, healthcare, legal, public-sector

4. **Data & Document Security** (2 pages) ✅
   - Location: `/pages/data-document-security/`
   - layered-security, layered-security-training

5. **Other Pages** (2 pages) ✅
   - Location: `/pages/other/`
   - glossary-of-terms, solution-assessment-questions

### Assets Created:

- **CSS:** 6 vendor + 2 core files (wordpress-extracted.css, banner-fix.css)
- **JS:** 12 vendor + 1 loader (component-loader.js)
- **Images:** 77+ files in `/assets/images/content/`
- **Components:** header.html, nav.html, footer.html

---

## 🚧 REMAINING WORK (~18 pages = 45%)

### Priority Order:

1. **Graphic Communications** (~6 pages)
   - `graphic-communications/AccurioPro-Solutions/`
   - `graphic-communications/e-Commerce/`
   - `graphic-communications/Management-Information-Systems/`
   - `graphic-communications/Transactional-Variable-Data-Printing/`
   - `graphic-communications/Variable-Data-Printing/`
   - `graphic-communications/Workflow-Solutions/`

2. **Supported Solutions** (~10 pages)
   - **Cloud:** `support/Cloud/` - Device-Management, Print-Management, Visitor-Management (3 pages)
   - **On-Premises:** `support/On-Premises/` - Device-Management, Document-Management, Fax-Solutions, Intelligent-Document-Processing, Pay-for-Print, Print-Management, Visitor-Management (7 pages)

3. **Other Remaining** (~2 pages)
   - Index page(s)
   - Any other WordPress exports not yet refactored

---

## 📐 ESTABLISHED WORKFLOW

### The Process (Works Perfectly):

1. **Analyze Section**

   ```bash
   find SECTION_FOLDER -name "*.html" ! -name "*_files*" | sort
   ```

2. **Copy Unique Images** (with deduplication)

   ```bash
   find SECTION -name "*_files" -type d | while read dir; do
     find "$dir" -maxdepth 1 \( -name "*.jpg" -o -name "*.png" -o -name "*.svg" \) \
       ! -name "logo*" ! -name "giving-shapes*" ! -name "embed*" ! -name "saved*" \
       | while read img; do cp "$img" assets/images/content/ 2>/dev/null; done
   done
   ```

3. **Create Output Directory**

   ```bash
   mkdir -p pages/SECTION_NAME
   ```

4. **Use Subagent to Refactor**
   - Batch process all pages in section
   - Apply standard template
   - Fix image paths
   - Remove tracking scripts

5. **Verify Quality**

   ```bash
   # Check banner-fix.css included
   grep -l "banner-fix.css" pages/SECTION/*.html | wc -l

   # Check for old paths (should be 0)
   grep -h "_files\|gtm\.js\|bugherd" pages/SECTION/*.html
   ```

### Deduplication Works Automatically

- CSS/JS files checked via `diff -q` before copying
- Images copied with `cp 2>/dev/null` (fails silently if exists)
- **Result:** No bloat, all pages share assets

---

## 📋 STANDARD TEMPLATE

Every refactored page uses this structure:

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>PAGE_TITLE - Konica Minolta</title>
    <link
      rel="icon"
      type="image/png"
      sizes="32x32"
      href="/assets/images/icons/favicon-32x32.png" />

    <!-- Global CSS - Vendor -->
    <link rel="stylesheet" href="/assets/css/vendor/bootstrap.min.css" />
    <link rel="stylesheet" href="/assets/css/vendor/plugin.css" />
    <link rel="stylesheet" href="/assets/css/vendor/utilities.css" />
    <link rel="stylesheet" href="/assets/css/vendor/vendor.css" />
    <link rel="stylesheet" href="/assets/css/vendor/style.css" />

    <!-- Global CSS - Core -->
    <link rel="stylesheet" href="/assets/css/core/wordpress-extracted.css" />
    <link rel="stylesheet" href="/assets/css/core/banner-fix.css" />
  </head>

  <body class="BODY_CLASS">
    <!-- Component containers -->
    <div id="header-container"></div>
    <div id="nav-container"></div>

    <!-- PAGE-SPECIFIC CONTENT HERE -->

    <!-- Footer component -->
    <div id="footer-container"></div>

    <!-- Global JS -->
    <script src="/assets/js/vendor/jquery.min.js"></script>
    <script src="/assets/js/vendor/jquery-migrate.min.js"></script>
    <script src="/assets/js/vendor/bootstrap.min.js"></script>
    <script src="/assets/js/vendor/plugin.js"></script>
    <script src="/assets/js/vendor/vendor.js"></script>
    <script src="/assets/js/component-loader.js"></script>
  </body>
</html>
```

### Key Points:

- **banner-fix.css** is REQUIRED (fixes hero banner overlay issue)
- **Body classes** vary: `bg-teal`, `bg-sage-green`, `bg-pink`, `default`, etc.
- **Component containers** must have exact IDs: `header-container`, `nav-container`, `footer-container`

---

## 🔧 TRANSFORMATIONS APPLIED

### What We Remove:

- ❌ All `<style>` inline CSS tags → extracted to wordpress-extracted.css
- ❌ All `<script>` inline JavaScript
- ❌ Google Tag Manager (GTM) scripts
- ❌ BugHerd tracking scripts
- ❌ WordPress header/footer/navigation HTML
- ❌ Inline `style=""` attributes (especially on banner elements)

### What We Fix:

- ✅ Image paths: `./FOLDER_files/image.jpg` → `/assets/images/content/image.jpg`
- ✅ CDN URLs: `https://solutionsmkm.b-cdn.net/wp-content/uploads/...` → `/assets/images/content/filename.ext`
- ✅ WordPress URLs: `https://solutionsguide.mykonicaminolta.com/...` → `/` or relative paths
- ✅ Navigation links: Convert to relative (will be updated in final phase)

---

## 🐛 KNOWN ISSUES & SOLUTIONS

### 1. ✅ FIXED: Banner Text Below Image

**Issue:** Hero banner text appears below banner image instead of overlaying it.

**Solution:** Created `/assets/css/core/banner-fix.css`

```css
.heroslides .slides .bg-img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: 1;
}

.heroslides .caption {
  position: relative;
  z-index: 2;
  color: #fff;
  text-align: left; /* User preference: left-aligned */
  padding: 40px 20px;
}
```

**Status:** All pages include banner-fix.css automatically.

### 2. ⚠️ PENDING: Navigation Links Non-Functional

**Issue:** Navigation menu links point to old WordPress URLs.

**Why:** Intentionally deferred until ALL pages refactored.

**Plan:**

1. Complete all refactoring first
2. Create URL mapping document: `old URL → new URL`
3. Update `/components/nav.html` once with all correct paths
4. One update fixes all 40+ pages (benefit of component system!)

**Timeline:** After all pages refactored (Phase 4).

---

## 📁 FILE STRUCTURE

```
ops-solutions-playbook/
├── assets/                          # SHARED by all pages
│   ├── css/
│   │   ├── vendor/                  # 6 files (Bootstrap, plugins, etc.)
│   │   └── core/
│   │       ├── wordpress-extracted.css  # All WordPress inline CSS
│   │       └── banner-fix.css           # Hero banner positioning fix
│   ├── js/
│   │   ├── vendor/                  # 12 files (jQuery, Bootstrap, etc.)
│   │   └── component-loader.js      # Injects header/nav/footer
│   └── images/
│       ├── logos/                   # Logo files
│       ├── icons/                   # Favicons
│       └── content/                 # 77+ content images (deduplicated)
│
├── components/                      # SHARED components
│   ├── header.html                  # Logo, no search bar
│   ├── nav.html                     # Full menu (links not yet updated)
│   └── footer.html                  # Simple copyright footer
│
├── pages/                           # REFACTORED pages
│   ├── core/
│   │   ├── cloud/                   # 7 pages ✅
│   │   └── on-premises/             # 7 pages ✅
│   ├── vertical/                    # 4 pages ✅
│   ├── data-document-security/      # 2 pages ✅
│   └── other/                       # 2 pages ✅
│
├── core/                            # ❌ ORIGINAL WordPress exports
├── vertical/                        # ❌ ORIGINAL WordPress exports
├── layered-security/                # ❌ ORIGINAL WordPress exports
├── graphic-communications/          # ⏳ TODO
├── support/                         # ⏳ TODO
│
├── REFACTORING-GUIDE.md             # Progress tracking & navigation plan
├── QA-CHECKLIST.md                  # Per-page testing checklist
├── HANDOFF.md                       # 👈 THIS FILE
└── pages/index.html                 # Main template example
```

---

## 🚀 HOW TO CONTINUE (NEW CHAT SESSION)

### Step 1: Review Current State

```bash
# See what's done
ls -R pages/

# Count completed pages
find pages -name "*.html" -type f | wc -l

# Check asset count
ls assets/images/content/*.{jpg,png,svg} 2>/dev/null | wc -l
```

### Step 2: Pick Next Section

Recommended order:

1. **Graphic Communications** (6 pages) - Similar structure to previous work
2. **Supported Solutions** (10 pages) - Largest remaining section
3. **Other remaining** - Anything left

### Step 3: Use Established Workflow

Follow the 5-step process documented above:

1. Find HTML files
2. Copy images with deduplication
3. Create output directory
4. Use subagent to batch refactor
5. Verify quality

### Step 4: Subagent Prompt Template

Use this proven template for subagent:

```
I need you to extract and refactor [N] WordPress HTML files from [SECTION] into clean pages.

**CONTEXT:**
- Successfully refactored 22 pages so far
- Using consistent template structure and component system
- All CSS/JS assets in /assets/ (deduplicated)
- All images in /assets/images/content/
- banner-fix.css working perfectly

**FILES TO PROCESS:**
[List source → destination mappings]

**TEMPLATE:**
[Use standard template from HANDOFF.md]

**TRANSFORMATIONS:**
1. Extract content between nav and footer
2. Fix image paths to /assets/images/content/
3. Remove GTM, BugHerd, tracking scripts
4. Fix WordPress URLs to relative paths
5. Include banner-fix.css

**VERIFICATION:**
- No CDN URLs remaining
- No old ./FOLDER_files/ paths
- No tracking scripts
- banner-fix.css included
```

---

## 📊 QUALITY METRICS

### Success Criteria for Each Page:

- ✅ Uses standard template structure
- ✅ All CSS/JS externalized (no inline)
- ✅ banner-fix.css included
- ✅ Component containers present
- ✅ Image paths fixed to /assets/images/content/
- ✅ No tracking scripts
- ✅ Body class preserved
- ✅ Line count: ~200-800 lines (vs. original 1,000-3,000)

### Testing Each Page:

```bash
# Start local server
python3 -m http.server 8000

# Test page
open http://localhost:8000/pages/SECTION/PAGENAME.html

# Visual checks:
# - Header loads (logo visible)
# - Nav dropdowns work (links don't work yet - expected)
# - Banner text overlays image (not below)
# - Content displays correctly
# - Footer appears at bottom
# - No console errors in DevTools
```

---

## 💡 TIPS & PATTERNS

### Image Path Patterns

```
# WordPress exports use these patterns:
./Device Management_files/image.jpg
https://solutionsmkm.b-cdn.net/wp-content/uploads/2019/03/image.jpg

# We convert to:
/assets/images/content/image.jpg
```

### Body Classes Seen

- `default` - Most common, white background
- `bg-teal` - Teal background (Cloud pages)
- `bg-sage-green` - Green background (Vertical pages)
- `bg-pink` - Pink background (Solution Assessment)
- `bg-light-blue` - Light blue (Glossary)

### Subagent Efficiency

- Processes 6-7 pages in ~3-5 minutes
- Consistent quality across batch
- Automatic verification built-in
- Better than manual one-by-one

---

## 📝 FINAL PHASE: NAVIGATION UPDATE

**Do THIS LAST** (after all pages refactored):

1. **Create URL Mapping Document**

   ```
   OLD → NEW
   /core-solutions/device-management-cloud/ → /pages/core/cloud/device-management.html
   /vertical/finance/ → /pages/vertical/finance.html
   [etc. for all pages]
   ```

2. **Update `/components/nav.html`**
   - Replace all old WordPress URLs with new paths
   - One update = all pages fixed (component benefit!)

3. **Test Navigation**
   - Click through every menu item
   - Verify all links work
   - Test mobile dropdown

4. **Full Site QA**
   - All pages load
   - All navigation functional
   - Cross-page links work

---

## 🎯 SUCCESS METRICS

### Current Progress:

- **22 pages refactored** (55%)
- **~18 pages remaining** (45%)
- **77+ images** deduplicated
- **0 duplicate CSS/JS** files
- **~8,500+ lines** of clean code

### When Complete:

- ~40 clean, maintainable pages
- 85%+ code reduction
- Single set of shared assets
- Easy updates (change component = all pages update)
- Fast loading (deduplicated assets)
- Clean git history

---

## 🆘 IF SOMETHING BREAKS

### Banner Text Below Image

Check: Is `banner-fix.css` included in `<head>`?

### Components Not Loading

Check: Using web server? (not file://)

```bash
python3 -m http.server 8000
```

### Images Not Displaying

Check: Paths use `/assets/images/content/` not `./FOLDER_files/`

### Duplicate Assets

Run deduplication check:

```bash
# Check for duplicates
find assets/images/content -type f | sort | uniq -d
```

---

## ✅ READY FOR HANDOFF

This document contains everything needed to continue the refactoring project in a new chat session. The workflow is proven, the templates are established, and the remaining sections follow the same patterns as completed work.

**Next Steps:**

1. Start new chat
2. Share this HANDOFF.md
3. Continue with Graphic Communications
4. Follow established workflow
5. Complete remaining ~18 pages
6. Update navigation (final step)
7. Full site QA
8. Ship it! 🚀

---

**Questions?** Refer to:

- `REFACTORING-GUIDE.md` - Detailed progress & navigation plan
- `QA-CHECKLIST.md` - Testing procedures
- `REFACTOR-README.md` - Original one-shot refactor documentation
