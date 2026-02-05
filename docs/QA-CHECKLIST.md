# Page QA Checklist

Use this checklist to test each refactored page individually during the refactoring process.

---

## 🧪 Per-Page Testing (Before Navigation Update)

### Setup

```bash
# Start local server in project root
cd /Users/bradleypierce/Developer/ops-solutions-playbook
python3 -m http.server 8000

# Open browser to
http://localhost:8000/pages/core/cloud/PAGENAME.html
```

### Visual Checks ✓

- [ ] **Page Loads**: No 404 errors, page displays
- [ ] **Header**: Logo appears at top
- [ ] **Navigation**: Dropdown menus visible (links may not work yet - OK)
- [ ] **Hero Banner**:
  - [ ] Banner image displays
  - [ ] ✅ **Text overlays the image** (not below it)
  - [ ] Text is readable (white text on image)
  - [ ] Horizontal line (hr) appears under heading
- [ ] **Content Sections**: All text content displays properly
- [ ] **Images**: All product logos and content images load
- [ ] **Sidebar**: Benefits/features sidebar displays correctly
- [ ] **Footer**: Footer appears with copyright text
- [ ] **No Console Errors**: Open DevTools (F12) - no red errors

### Browser Console (F12)

Look for these success messages:

```
✓ Loaded /components/header.html
✓ Loaded /components/nav.html
✓ Loaded /components/footer.html
```

### Expected Issues (OK to Ignore for Now)

- ⚠️ **Navigation links don't work** - This is expected
- ⚠️ **Clicking nav items may show 404** - Navigation update comes later
- ⚠️ **Breadcrumbs link to old URLs** - Will fix with navigation

### Critical Issues (Must Fix)

- ❌ Banner text below image instead of on top
- ❌ Images not loading (check path in src attribute)
- ❌ Components not loading (header/nav/footer missing)
- ❌ Console errors about missing files

---

## 📋 Batch Testing Record

### Core/Cloud Pages

| Page                                 | Loads | Banner OK | Images OK | Components OK | Date Tested | Notes |
| ------------------------------------ | ----- | --------- | --------- | ------------- | ----------- | ----- |
| device-management.html               | ☐     | ☐         | ☐         | ☐             |             |       |
| document-management.html             | ☐     | ☐         | ☐         | ☐             |             |       |
| fax-solutions.html                   | ☐     | ☐         | ☐         | ☐             |             |       |
| intelligent-document-processing.html | ☐     | ☐         | ☐         | ☐             |             |       |
| konica-minolta-marketplace.html      | ☐     | ☐         | ☐         | ☐             |             |       |
| print-management.html                | ☐     | ☐         | ☐         | ☐             |             |       |
| security.html                        | ☐     | ☐         | ☐         | ☐             |             |       |

### Core/On-Premises Pages

| Page                                 | Loads | Banner OK | Images OK | Components OK | Date Tested | Notes |
| ------------------------------------ | ----- | --------- | --------- | ------------- | ----------- | ----- |
| device-management.html               | ☐     | ☐         | ☐         | ☐             |             |       |
| intelligent-document-processing.html | ☐     | ☐         | ☐         | ☐             |             |       |
| integrated-option-solutions.html     | ☐     | ☐         | ☐         | ☐             |             |       |
| mobile-applications.html             | ☐     | ☐         | ☐         | ☐             |             |       |
| pdf-editing.html                     | ☐     | ☐         | ☐         | ☐             |             |       |
| print-management.html                | ☐     | ☐         | ☐         | ☐             |             |       |
| security.html                        | ☐     | ☐         | ☐         | ☐             |             |       |

---

## 🧭 Full Site Navigation Testing (After All Refactoring)

**Do NOT perform this until ALL pages are refactored and navigation is updated!**

### Navigation Testing

- [ ] **Core Solutions > Cloud**: All 7 links work
- [ ] **Core Solutions > On-Premises**: All 7 links work
- [ ] **Vertical**: All 4 links work
- [ ] **Graphic Communications**: All 6 links work
- [ ] **Data & Document Security**: All 2 links work
- [ ] **Supported Solutions**: All links work
- [ ] **Glossary/Index**: Direct links work

### Cross-Page Testing

- [ ] Navigate from Homepage → Cloud page → Different section
- [ ] Click breadcrumbs (if applicable)
- [ ] Test all internal links within content
- [ ] Search functionality (if present)

### Mobile Testing

- [ ] Open on mobile device or responsive mode (DevTools)
- [ ] Navigation hamburger menu works
- [ ] Pages are readable on small screens
- [ ] Images scale properly
- [ ] Touch targets are adequate size

### Browser Compatibility

- [ ] Chrome/Edge
- [ ] Firefox
- [ ] Safari (if on Mac)

---

## 📊 Testing Summary Template

```markdown
## Testing Session - [Date]

**Pages Tested:** X pages
**Issues Found:** Y issues
**Status:** ✅ Pass / ⚠️ Issues / ❌ Fail

### Issues:

1. [Issue description] - [Severity: Critical/Medium/Low]
2. [Issue description] - [Severity: Critical/Medium/Low]

### Notes:

- [Any observations]
```

---

## 🔍 Troubleshooting Common Issues

### Banner Text Below Image

**Cause:** Missing banner-fix.css
**Fix:** Add `<link rel="stylesheet" href="/assets/css/core/banner-fix.css" />` to `<head>`

### Components Not Loading

**Cause:** Not using web server (opened file:// instead of http://)
**Fix:** Use `python3 -m http.server 8000` and access via http://localhost:8000

### Images Not Loading

**Cause:** Wrong path in src attribute
**Fix:** Check that path is `/assets/images/content/IMAGE.jpg` (not `./FOLDER_files/`)

### Console Error: "Failed to load component"

**Cause:** Component files missing or wrong path
**Fix:** Verify `/components/header.html`, `nav.html`, `footer.html` exist

---

## ✅ Sign-Off

Once all checks pass for a page, mark it complete here:

**Completed Pages:**

- [ ] pages/core/cloud/device-management.html
- [ ] pages/core/cloud/document-management.html
- [ ] pages/core/cloud/fax-solutions.html
- [ ] pages/core/cloud/intelligent-document-processing.html
- [ ] pages/core/cloud/konica-minolta-marketplace.html
- [ ] pages/core/cloud/print-management.html
- [ ] pages/core/cloud/security.html

**Tested By:** ******\_\_\_******
**Date:** ******\_\_\_******
