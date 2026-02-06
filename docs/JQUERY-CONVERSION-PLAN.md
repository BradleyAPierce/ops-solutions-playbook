# jQuery Conversion Plan

**Last Updated:** February 6, 2026  
**Status:** Planning Phase - jQuery dependencies identified

This document outlines the plan for removing jQuery dependencies and migrating to vanilla JavaScript.

---

## 📊 Current jQuery Usage

### Files Using jQuery

**Vendor Files (Current):**

- `/assets/js/vendor/jquery.min.js` (v3.x)
- `/assets/js/vendor/jquery-migrate.min.js`
- `/assets/js/vendor/vendor.js` (may contain jQuery plugins)
- `/assets/js/vendor/plugin.js` (may contain jQuery dependencies)

**All HTML Pages Reference jQuery:**

- 40+ pages include: `<script src="assets/js/vendor/jquery.min.js"></script>`
- All pages load jQuery before other vendor scripts

---

## 🎯 Conversion Goals

1. **Remove jQuery dependency** from all pages
2. **Convert jQuery plugins** to vanilla JavaScript alternatives
3. **Update vendor.js and plugin.js** to remove jQuery dependencies
4. **Reduce page weight** by ~85KB (jQuery + migrate)
5. **Improve performance** with native browser APIs
6. **Maintain compatibility** with existing functionality

---

## 🔍 Analysis Required

### Step 1: Identify jQuery Usage Patterns

**Actions Needed:**

- [ ] Audit `vendor.js` for jQuery plugin usage
- [ ] Audit `plugin.js` for jQuery dependencies
- [ ] Search all HTML pages for inline jQuery code
- [ ] Identify Bootstrap version and jQuery requirements
- [ ] Document all DOM manipulation patterns

**Command to find jQuery usage:**

```bash
# Search for jQuery patterns in JavaScript files
grep -r "\$(" assets/js/ --include="*.js"
grep -r "jQuery(" assets/js/ --include="*.js"

# Search for inline jQuery in HTML
grep -r "\$(this)" pages/ --include="*.html"
grep -r "\$(function()" pages/ --include="*.html"
grep -r "jQuery" pages/ --include="*.html"
```

---

## 🗺️ Migration Strategy

### Phase 1: Audit & Document (Week 1)

- [ ] Complete usage analysis (see Step 1 above)
- [ ] Document all jQuery plugin dependencies
- [ ] Identify vanilla JS alternatives
- [ ] Create detailed conversion checklist
- [ ] Estimate effort per component

### Phase 2: Bootstrap Migration (Week 2)

**Current:** Bootstrap 4.x (requires jQuery)  
**Target:** Bootstrap 5.3+ (vanilla JS)

- [ ] Upgrade Bootstrap to v5.3.x
- [ ] Update Bootstrap JS references
- [ ] Test all Bootstrap components (modals, dropdowns, carousels, etc.)
- [ ] Remove bootstrap.min.js jQuery dependency

### Phase 3: Plugin Conversion (Week 3-4)

Convert or replace jQuery plugins:

- [ ] **Sliders/Carousels**: Replace with Swiper.js or native CSS
- [ ] **Animations**: Replace with GSAP or CSS animations
- [ ] **AJAX**: Convert to fetch API
- [ ] **Event handlers**: Convert to addEventListener
- [ ] **DOM manipulation**: Convert to vanilla JS methods

### Phase 4: Custom Code Migration (Week 5)

- [ ] Convert inline jQuery in HTML pages
- [ ] Refactor vendor.js jQuery dependencies
- [ ] Refactor plugin.js jQuery code
- [ ] Update component-loader.js (already vanilla JS ✓)

### Phase 5: Testing & Validation (Week 6)

- [ ] Cross-browser testing (Chrome, Firefox, Safari, Edge)
- [ ] Mobile/tablet responsive testing
- [ ] Functionality testing for all interactive elements
- [ ] Performance benchmarking
- [ ] Accessibility validation

### Phase 6: Cleanup & Deployment (Week 7)

- [ ] Remove jQuery files from vendor directory
- [ ] Remove jQuery script tags from all HTML pages
- [ ] Update documentation
- [ ] Deploy changes
- [ ] Monitor for issues

---

## 🔧 Common Conversion Patterns

### jQuery → Vanilla JavaScript Reference

#### DOM Selection

```javascript
// jQuery
$(".class");
$("#id");
$("div");

// Vanilla JS
document.querySelectorAll(".class");
document.getElementById("id");
document.querySelectorAll("div");
```

#### Event Handling

```javascript
// jQuery
$('.btn').click(function() { ... })
$(document).ready(function() { ... })

// Vanilla JS
document.querySelectorAll('.btn').forEach(btn => {
  btn.addEventListener('click', function() { ... })
})
document.addEventListener('DOMContentLoaded', function() { ... })
```

#### AJAX Requests

```javascript
// jQuery
$.ajax({ url: '/api', success: function(data) { ... } })

// Vanilla JS
fetch('/api')
  .then(response => response.json())
  .then(data => { ... })
```

#### CSS Manipulation

```javascript
// jQuery
$(".element").addClass("active");
$(".element").css("color", "red");

// Vanilla JS
document.querySelector(".element").classList.add("active");
document.querySelector(".element").style.color = "red";
```

#### DOM Manipulation

```javascript
// jQuery
$(".container").append("<div>New</div>");
$(".element").remove();

// Vanilla JS
document
  .querySelector(".container")
  .insertAdjacentHTML("beforeend", "<div>New</div>");
document.querySelector(".element").remove();
```

---

## 📦 Recommended Libraries (jQuery-Free)

### For Specific Functionality

| Need          | Recommendation | Size        | Notes                     |
| ------------- | -------------- | ----------- | ------------------------- |
| Carousels     | Swiper.js      | ~40KB       | Modern, mobile-friendly   |
| Animations    | GSAP           | ~45KB       | Professional animations   |
| HTTP Requests | Axios / Fetch  | ~13KB / 0KB | Axios or native Fetch API |
| Utilities     | Lodash-ES      | ~4KB/fn     | Tree-shakeable utilities  |
| Date/Time     | Day.js         | ~7KB        | Moment.js alternative     |
| Modals        | Micromodal     | ~3KB        | Lightweight, accessible   |

**Note:** Bootstrap 5+ includes all necessary modal, dropdown, and collapse functionality without jQuery.

---

## ⚠️ Breaking Changes to Watch For

1. **Event Delegation**: jQuery's `.on()` with delegation needs careful conversion
2. **Animation Callbacks**: jQuery animation complete callbacks need conversion
3. **Plugin Dependencies**: Third-party plugins may require jQuery
4. **Legacy Browser Support**: Consider polyfills if supporting IE11
5. **Bootstrap Components**: Must upgrade to Bootstrap 5+ simultaneously

---

## 📈 Performance Benefits

### Expected Improvements

- **Page Load Time**: -85KB (jQuery 3.x + migrate)
- **Parse Time**: ~15-20ms faster on mobile
- **Memory Usage**: ~10-15% reduction
- **Time to Interactive**: ~50-100ms improvement

---

## ✅ Progress Tracker

### Overall Progress: 0% Complete

- [ ] Phase 1: Audit & Document (0%)
- [ ] Phase 2: Bootstrap Migration (0%)
- [ ] Phase 3: Plugin Conversion (0%)
- [ ] Phase 4: Custom Code Migration (0%)
- [ ] Phase 5: Testing & Validation (0%)
- [ ] Phase 6: Cleanup & Deployment (0%)

---

## 📚 Resources

### Documentation

- [You Might Not Need jQuery](http://youmightnotneedjquery.com/)
- [Bootstrap 5 Migration Guide](https://getbootstrap.com/docs/5.3/migration/)
- [MDN Web Docs - Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)
- [Vanilla JS Toolkit](https://vanillajstoolkit.com/)

### Tools

- [jQuery to Vanilla JS Converter](https://tobiasahlin.com/blog/move-from-jquery-to-vanilla-javascript/)
- [Bundle Size Analyzer](https://bundlephobia.com/)

---

## 🔄 Rollback Plan

If issues arise during conversion:

1. **Git Branch Strategy**: All work in feature branch `jquery-removal`
2. **Keep jQuery Files**: Don't delete until fully tested
3. **Incremental Deployment**: Convert page-by-page if needed
4. **Feature Flags**: Consider toggle for old vs new code
5. **Monitoring**: Watch error logs after deployment

---

## 👥 Team Notes

### Before Starting

- Review this plan with development team
- Allocate appropriate time for testing
- Set up staging environment for validation
- Communicate timeline to stakeholders

### During Migration

- Commit frequently with clear messages
- Test each component after conversion
- Document any unexpected issues
- Update this document with findings

### After Completion

- Update [REFACTORING-GUIDE.md](REFACTORING-GUIDE.md) with jQuery removal notes
- Update [QA-CHECKLIST.md](QA-CHECKLIST.md) with new test cases
- Archive this document or mark as complete

---

**Next Steps:**

1. Run audit commands (see Phase 1)
2. Schedule team review meeting
3. Create feature branch: `git checkout -b jquery-removal`
4. Begin Phase 1 analysis
