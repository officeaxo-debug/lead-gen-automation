# Weekly Blog Post Automation

Automatically generates SEO/AEO optimized blog posts for all 7 domains and uploads them via FTP every week.

## What It Does

- **Generates unique blog posts** for each domain's niche (retirement villages, epoxy floors, real estate, etc.)
- **SEO optimized** with proper H1, meta tags, local keywords
- **AEO ready** with proper schema, citations, authoritative tone
- **Auto-uploads** via FTP to `{domain}/public_html/blog/`
- **Runs weekly** every Monday at 9 AM UTC (5 PM AEST)

## Files

- `blog_generator.py` — Python script that generates and uploads posts
- `domains.json` — Configuration with all 7 domains + FTP credentials
- `.github/workflows/weekly-blog.yml` — GitHub Actions scheduled workflow
- `blog_generation_log.json` — Results log (generated after each run)

## Setup

### 1. Upload to Your GitHub Repository

```bash
# Copy these files to your GitHub repo root:
- blog_generator.py
- domains.json
- .github/workflows/weekly-blog.yml
- README.md (this file)

git add .
git commit -m "Setup weekly blog automation"
git push
```

### 2. Add Anthropic API Key to GitHub Secrets

1. Go to your GitHub repo
2. **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. **Name:** `ANTHROPIC_API_KEY`
5. **Value:** Your Anthropic API key (from https://console.anthropic.com)
6. Click **Add secret**

### 3. Verify the Workflow

1. Go to **Actions** tab in GitHub
2. Select **Weekly Blog Post Generation**
3. Click **Run workflow** → **Run workflow** (to test immediately)
4. Wait ~2 minutes for completion
5. Check the run logs to see results

## How It Works

1. **Schedule:** Runs every Monday at 9 AM UTC
2. **For each domain:**
   - Researches the niche (retirement villages, epoxy floors, etc.)
   - Generates a unique 1500-2000 word blog post
   - Creates proper HTML with schema markup
   - Uploads via FTP to `public_html/blog/`
3. **Logs results** in `blog_generation_log.json`

## Blog Post Features

Each post includes:
- ✅ SEO-optimized title (H1)
- ✅ Meta description (155-160 chars)
- ✅ 1500-2000 word body with H2 sections
- ✅ FAQ section
- ✅ Local keywords (Gold Coast, Townsville, Mackay, etc.)
- ✅ Service-specific details
- ✅ BlogPosting JSON-LD schema
- ✅ LocalBusiness schema
- ✅ AEO readiness (clear claims, cited sources)
- ✅ Call-to-action

## Manual Trigger

To generate blogs on-demand (not on schedule):

1. Go to **Actions** tab
2. Select **Weekly Blog Post Generation**
3. Click **Run workflow**
4. Select branch (main)
5. Click **Run workflow**

Blogs will be generated and uploaded within 2-3 minutes.

## FTP Credentials (Stored Securely)

All FTP credentials are stored in `domains.json` and are only accessible via GitHub Actions. Never commit credentials to a public repo.

Current setup:
- **FTP Host:** `ftp://145.79.14.75`
- **Domains:** 7 (all on same Hostinger account)
- **Upload Path:** `public_html/blog/`
- **Password:** Same for all (`Blog2025Auto!`)

## Monitoring

After each run, check:
1. **GitHub Actions logs** → Latest run for any errors
2. **FTP server** → New posts in `{domain}/public_html/blog/`
3. **blog_generation_log.json** → Detailed results

## Troubleshooting

### FTP Upload Fails
- Check FTP credentials in `domains.json`
- Verify `public_html` directory exists on Hostinger
- Ensure blog directory is writable

### API Errors
- Verify `ANTHROPIC_API_KEY` secret is set correctly
- Check that API key is valid and has credits
- Review GitHub Actions logs for specific error

### No Posts Generated
- Check GitHub Actions workflow status
- Verify `domains.json` is valid JSON
- Review workflow logs for error messages

## Cost

- **Claude API:** ~$2-5 per week (7 posts at 1500-2000 words each)
- **GitHub Actions:** Free (unlimited for public repos)
- **Hostinger FTP:** Included with your plan

Total: ~$10-20/month for automated blog content

## Schedule

Blogs generate:
- **Frequency:** Every Monday at 9 AM UTC
- **Time:** ~2-3 minutes per run
- **Posts per run:** 7 (one per domain)

Change the schedule in `.github/workflows/weekly-blog.yml`:
```yaml
schedule:
  - cron: '0 9 * * 1'  # 9 AM UTC every Monday
```

Use cron format: `minute hour day_of_month month day_of_week`

## Next Steps

1. ✅ Upload files to GitHub
2. ✅ Add API key to secrets
3. ✅ Test with manual run
4. ✅ Monitor first week of posts
5. ✅ Adjust schedule/prompts if needed

Questions? Check the logs in GitHub Actions.
