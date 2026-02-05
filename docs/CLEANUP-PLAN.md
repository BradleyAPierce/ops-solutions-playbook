# Cleanup Plan - Post-Refactoring

**Status:** Documentation and Navigation Complete  
**Ready For:** File cleanup and final organization

---

## 📊 Summary

### ✅ Completed

- **40/40 pages refactored** and in `/pages/` directory
- **Navigation updated** - all links working
- **Documentation updated** - HANDOFF.md and REFACTORING-GUIDE.md current
- **Assets deduplicated** - 115+ images, all CSS/JS centralized

### 🗑️ Ready for Cleanup

- **139 MB** of original WordPress exports can be archived/deleted
- **5 utility scripts** used during refactoring
- **1 test file** (test-accordion.html)
- **Original index folder** no longer needed

---

## 📁 Files & Directories to Archive/Delete

### Original WordPress Export Folders (139 MB total)

**Safe to delete after backup:**

| Directory                        | Size   | Pages     | Status                                            |
| -------------------------------- | ------ | --------- | ------------------------------------------------- |
| `core/`                          | 48 MB  | 14 pages  | ✅ Refactored to `/pages/core/`                   |
| `support/`                       | 35 MB  | 10 pages  | ✅ Refactored to `/pages/support/`                |
| `graphic-communications/`        | 22 MB  | 8 pages   | ✅ Refactored to `/pages/graphic-communications/` |
| `vertical/`                      | 16 MB  | 4 pages   | ✅ Refactored to `/pages/vertical/`               |
| `layered-security/`              | 8.1 MB | 2 pages   | ✅ Refactored to `/pages/data-document-security/` |
| `glossary-of-terms/`             | 3.3 MB | 1 page    | ✅ Refactored to `/pages/other/`                  |
| `solution-assessment-questions/` | 3.3 MB | 1 page    | ✅ Refactored to `/pages/other/`                  |
| `index/`                         | 3.4 MB | Old index | ✅ No longer needed                               |

**All contain:**

- Original WordPress HTML exports (1,000-3,000 lines each)
- Duplicate CSS/JS in `*_files/` folders
- Duplicate images (already copied to `/assets/images/content/`)
- Inline styles and tracking scripts

---

### Utility Scripts (Root Directory)

**Python scripts used during refactoring:**

| File                                 | Purpose                             | Status           |
| ------------------------------------ | ----------------------------------- | ---------------- |
| `clean_word_artifacts.py`            | Removed Word artifacts from exports | ✅ Task complete |
| `format_html_files.py`               | HTML formatting utility             | ✅ Task complete |
| `refactor_cloud_pages.py`            | Automated Cloud page refactoring    | ✅ Task complete |
| `refactor_graphic_communications.py` | Automated GC refactoring            | ✅ Task complete |

**Recommendation:** Keep these scripts if you might refactor more WordPress exports in the future. Otherwise, can archive/delete.

---

### Test Files

| File                  | Purpose                         | Status            |
| --------------------- | ------------------------------- | ----------------- |
| `test-accordion.html` | Testing accordion functionality | ✅ Can be deleted |

---

## ✅ Files to KEEP

### Core Application Files

- **`/pages/`** - All 40 refactored pages ✅
- **`/assets/`** - All CSS, JS, images (deduplicated) ✅
- **`/components/`** - header.html, nav.html, footer.html ✅

### Documentation

- **`README.md`** - Project overview ✅
- **`HANDOFF.md`** - Updated with completion status ✅
- **`REFACTORING-GUIDE.md`** - Updated with all issues/solutions ✅
- **`REFACTOR-README.md`** - Original refactor documentation ✅
- **`QA-CHECKLIST.md`** - Testing procedures ✅
- **`CLOUD-REFACTOR-*.md`** - Historical refactor notes ✅
- **`CLEANUP-PLAN.md`** (this file) ✅

---

## 🔄 Recommended Cleanup Process

### Step 1: Create Backup (IMPORTANT!)

```bash
# Create backup of original WordPress exports
mkdir -p backup/wordpress-originals
mv core vertical support layered-security graphic-communications \
   glossary-of-terms solution-assessment-questions index backup/wordpress-originals/

# Date the backup
mv backup/wordpress-originals backup/wordpress-originals-2026-02-05
```

### Step 2: Archive Utility Scripts (Optional)

```bash
# If you want to keep them for reference
mkdir -p backup/refactoring-scripts
mv clean_word_artifacts.py format_html_files.py \
   refactor_cloud_pages.py refactor_graphic_communications.py \
   backup/refactoring-scripts/
```

### Step 3: Delete Test Files

```bash
rm test-accordion.html
```

### Step 4: Verify Application Still Works

```bash
# Start local server
python3 -m http.server 8000

# Test:
# - Navigate to http://localhost:8000/pages/core/cloud/device-management.html
# - Click through navigation menu
# - Verify all links work
# - Check multiple pages across different sections
```

### Step 5: Final Cleanup (After Verification)

```bash
# If you don't need backups on this machine
rm -rf backup/wordpress-originals-2026-02-05
rm -rf backup/refactoring-scripts

# Or compress for long-term storage
tar -czf wordpress-originals-2026-02-05.tar.gz backup/wordpress-originals-2026-02-05
```

---

## 📊 Storage Savings

**Before Cleanup:**

- Original WordPress folders: ~139 MB
- Refactored structure: ~15 MB (assets + pages + components)
- **Total:** ~154 MB

**After Cleanup:**

- Refactored structure only: ~15 MB
- **Savings:** ~139 MB (90% reduction)

---

## ✅ Post-Cleanup File Structure

```
ops-solutions-playbook/
├── assets/                 # 115+ images, 8 CSS, 13 JS files
│   ├── css/
│   ├── js/
│   └── images/
├── components/             # 3 reusable components
│   ├── header.html
│   ├── nav.html ← UPDATED WITH NEW URLs
│   └── footer.html
├── pages/                  # 40 clean refactored pages
│   ├── core/
│   │   ├── cloud/ (7)
│   │   └── on-premises/ (7)
│   ├── support/
│   │   ├── cloud/ (3)
│   │   └── on-premises/ (7)
│   ├── vertical/ (4)
│   ├── graphic-communications/ (8)
│   ├── data-document-security/ (2)
│   └── other/ (2)
├── *.md                    # Documentation files
└── backup/ (optional)      # Archived originals
```

---

## 🎯 Next Steps After Cleanup

1. **Full Site QA**
   - Test all 40 pages
   - Verify all navigation links
   - Check mobile responsiveness
   - Test in multiple browsers

2. **Performance Optimization**
   - Minify CSS/JS if needed
   - Optimize images
   - Enable compression
   - Set up caching headers

3. **Deployment Preparation**
   - Choose hosting platform
   - Set up domain/DNS
   - Configure server settings
   - Create deployment guide

4. **Final Documentation**
   - Update README.md with deployment info
   - Document any custom configurations
   - Create maintenance guide

---

## ⚠️ Important Notes

**Before deleting anything:**

- ✅ Verify all 40 pages work correctly
- ✅ Test navigation thoroughly
- ✅ Create backups of originals
- ✅ Ensure all images copied to `/assets/images/content/`
- ✅ Confirm no broken links

**The original WordPress exports are the ONLY backup of:**

- Original page content
- Original image assets
- Original structure

**Keep backups** until you're 100% confident the refactored site is production-ready.

---

## 📞 Questions?

Refer to:

- `HANDOFF.md` - Current project status
- `REFACTORING-GUIDE.md` - Issues and solutions
- `QA-CHECKLIST.md` - Testing procedures

---

**Ready to proceed with cleanup? Follow the steps above carefully!**
