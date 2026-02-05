# Refactoring Guide & Known Issues

This document tracks known issues discovered during refactoring and provides a roadmap for completing the project.

---

## 🔧 Known Issues & Fixes

### 1. ✅ FIXED: Banner Text Positioning

**Issue:** Hero banner text appears below the image instead of overlaying it.

**Root Cause:**

- Original WordPress exports used inline styles: `style="background-image: url(...)"`
- During refactoring, inline styles were removed
- Banner images now display as `<img>` tags instead of CSS backgrounds

**Solution Applied:**
Created `/assets/css/core/banner-fix.css` with proper positioning:

- Background images positioned absolutely
- Caption overlay with z-index layering
- Responsive sizing maintained

**Status:** ✅ Fixed - Include banner-fix.css in all pages

**Testing:** Verify on device-management.html after adding CSS link

---

## 🔗 Navigation URL Updates

### Current Status: ⚠️ Pending

**Issue:** Navigation links point to old WordPress structure.

**Current URLs (Example):**

```
/core/Cloud/Device-Management/
/core-solutions/device-management-cloud/
```

**Target URLs:**

```
/pages/core/cloud/device-management.html
/pages/core/on-premises/device-management.html
```

### Navigation Update Plan

**Phase 1: Complete All Refactoring First** ⏳

- Finish refactoring all pages in:
  - ✅ Core/Cloud (7 pages) - DONE
  - ⏳ Core/On-Premises (7 pages) - TODO
  - ⏳ Vertical (4 pages) - TODO
  - ⏳ Graphic Communications (6 pages) - TODO
  - ⏳ Other sections - TODO

**Phase 2: Map All URLs** 📋
Create a mapping document:

```
Old URL → New URL
/core-solutions/device-management-cloud/ → /pages/core/cloud/device-management.html
/core-solutions/device-management-on-premises/ → /pages/core/on-premises/device-management.html
...
```

**Phase 3: Update Navigation Component** 🔗

- Update `/components/nav.html` with all new paths
- One update fixes all 40+ pages automatically (benefit of component system!)

**Phase 4: Testing & QA** ✅

- Test all navigation links
- Verify dropdowns work
- Check mobile navigation

### Why Wait Until Complete?

1. **Avoid Rework**: Don't update nav multiple times
2. **Complete Picture**: Know all final URLs before updating
3. **Efficient Testing**: Test all links in one QA pass
4. **Component Benefit**: One nav update = all pages fixed

### Recommended Approach

**For Now:**

- Continue refactoring remaining sections
- Document page names/URLs as you go
- Test pages individually without nav

**After All Refactoring:**

- Create comprehensive URL mapping
- Update nav.html once with all correct paths
- Run full site QA with working navigation

---

## 📝 Refactoring Checklist

### Completed Sections ✅

- [x] **Core/Cloud** (7 pages) - 86% reduction
  - [x] Device Management
  - [x] Document Management
  - [x] Fax Solutions
  - [x] Intelligent Document Processing
  - [x] Konica Minolta MarketPlace
  - [x] Print Management
  - [x] Security

### Remaining Sections ⏳

- [ ] **Core/On-Premises** (7 pages)
  - [ ] Device Management
  - [ ] Intelligent Document Processing
  - [ ] Integrated Option Solutions
  - [ ] Mobile Applications
  - [ ] PDF Editing
  - [ ] Print Management
  - [ ] Security

- [ ] **Vertical** (4 pages)
  - [ ] Finance
  - [ ] Healthcare
  - [ ] Legal
  - [ ] Public Sector

- [ ] **Graphic Communications** (6 pages)
  - [ ] AccurioPro Solutions
  - [ ] e-Commerce
  - [ ] Management Information Systems
  - [ ] Transactional Variable Data Printing
  - [ ] Variable Data Printing
  - [ ] Workflow Solutions

- [ ] **Data & Document Security** (2 pages)
  - [ ] Layered Security
  - [ ] Layered Security Training

- [ ] **Supported Solutions** (varies)
- [ ] **Other Pages** (Index, Glossary, etc.)

---

## 🎯 Testing Strategy

### Per-Page Testing (During Refactoring)

Test each refactored page individually:

- ✅ Page loads without errors
- ✅ Images display correctly
- ✅ Banner text overlays image
- ✅ Content sections render properly
- ✅ Footer displays correctly
- ⚠️ Skip navigation testing (links not updated yet)

**Test URL Pattern:**

```bash
# Start local server
python3 -m http.server 8000

# Test individual pages
http://localhost:8000/pages/core/cloud/device-management.html
http://localhost:8000/pages/core/cloud/document-management.html
```

### Full Site QA (After All Refactoring)

Complete end-to-end testing:

- ✅ All navigation links work
- ✅ Cross-page linking functional
- ✅ Search functionality (if applicable)
- ✅ Mobile responsiveness
- ✅ Browser compatibility
- ✅ Performance metrics

---

## 🔄 Automation & Workflow

### Subagent Usage

We're using VS Code subagents to efficiently process multiple pages:

**Benefits:**

- Processes 7+ pages in single operation
- Consistent transformations across all files
- Automatic path corrections
- Built-in verification

**When Used:**

- Batch refactoring of similar pages (e.g., all Cloud pages)
- Repetitive transformations
- Large-scale path corrections

**Process:**

1. Analyze first page manually
2. Create transformation template
3. Run subagent on batch
4. Verify output quality
5. Iterate if needed

---

## 📊 Progress Tracking

### Total Project Scope

- **Total Pages:** ~40 HTML files
- **Completed:** 7 pages (Core/Cloud)
- **Remaining:** ~33 pages
- **Progress:** 17.5%

### Asset Management

- **Images:** 30 files in /assets/images/content/
- **CSS Files:** 6 vendor + 2 core
- **JS Files:** 12 vendor + 1 loader
- **Deduplication:** ✅ Working (no asset copies)

---

## 🚀 Next Steps

1. **Fix Banner Issue Across All Cloud Pages**
   - Add banner-fix.css link to all 7 Cloud pages
   - Test each page
2. **Refactor Core/On-Premises**
   - 7 pages similar structure to Cloud
   - Use subagent for batch processing
3. **Continue with Remaining Sections**
   - Vertical (4 pages)
   - Graphic Communications (6 pages)
   - Others as needed

4. **Update Navigation (Final Step)**
   - Create URL mapping
   - Update nav.html
   - Full QA pass

---

## 💡 Tips for Continued Refactoring

1. **Copy Assets Once**: Check if images already exist before copying
2. **Batch Similar Pages**: Process similar structures together
3. **Document as You Go**: Note any unique issues per section
4. **Test Incrementally**: Verify pages work before moving on
5. **Save Often**: Commit to Git after each major section

---

## 📫 Questions or Issues?

Add new issues to this document as discovered during refactoring.
