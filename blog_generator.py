#!/usr/bin/env python3
"""
Weekly Blog Post Generator & Auto-Uploader
Generates SEO/AEO optimized blog posts and uploads via FTP to Hostinger
"""

import json
import os
import ftplib
from datetime import datetime
from anthropic import Anthropic

# Initialize Anthropic client
client = Anthropic()

# Load domain configuration
with open('domains.json', 'r') as f:
    config = json.load(f)

DOMAINS = config['domains']

def generate_blog_post(domain_info):
    """Generate a blog post for a domain using Claude"""
    domain_name = domain_info['domain']
    niche = domain_info['niche']
    service = domain_info['service']
    location = domain_info['location']
    
    prompt = f"""Generate a professional, SEO and AEO optimized blog post for a {service} business in {location}.

Domain: {domain_name}
Niche: {niche}

Requirements:
1. Title: Catchy, keyword-rich (H1)
2. Meta description: 155-160 chars
3. Body: 1500-2000 words
4. Structure: Intro, 3-4 main sections with H2s, FAQ, Conclusion
5. Include: Local keywords, service details, local landmarks, trust signals
6. Schema: BlogPosting + LocalBusiness JSON-LD
7. AI Search Readiness: Cite sources, clear claims, authoritative tone
8. Include call-to-action with phone/form details

Return ONLY valid HTML (no markdown, no code fences). Start with <!DOCTYPE html>.
Make it upload-ready for {domain_name}/public_html/blog/[filename].html"""

    print(f"🤖 Generating blog post for {domain_name}...")
    
    response = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=4000,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    html_content = response.content[0].text
    return html_content

def upload_to_ftp(domain_info, html_content):
    """Upload blog post to Hostinger via FTP"""
    ftp_host = domain_info['ftp_host']
    ftp_user = domain_info['ftp_username']
    ftp_pass = domain_info['ftp_password']
    domain_name = domain_info['domain']
    
    try:
        # Connect to FTP
        ftp = ftplib.FTP(ftp_host)
        ftp.login(ftp_user, ftp_pass)
        
        # Navigate to public_html/blog or create it
        ftp.cwd('public_html')
        
        # Try to create blog directory if it doesn't exist
        try:
            ftp.mkd('blog')
        except ftplib.all_errors:
            pass  # Directory might already exist
        
        ftp.cwd('blog')
        
        # Generate filename with date
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"post_{timestamp}.html"
        
        # Upload file
        ftp.storbinary(f'STOR {filename}', open('/tmp/blog_post.html', 'rb'))
        ftp.quit()
        
        print(f"✅ Uploaded {filename} to {domain_name}")
        return True
        
    except Exception as e:
        print(f"❌ FTP upload failed for {domain_name}: {str(e)}")
        return False

def main():
    """Generate and upload blog posts for all domains"""
    print("=" * 60)
    print("🚀 Weekly Blog Post Generator")
    print("=" * 60)
    
    results = {
        "generated_at": datetime.now().isoformat(),
        "posts": []
    }
    
    for domain_info in DOMAINS:
        try:
            # Generate blog post
            html_content = generate_blog_post(domain_info)
            
            # Save to temp file
            with open('/tmp/blog_post.html', 'w') as f:
                f.write(html_content)
            
            # Upload to FTP
            success = upload_to_ftp(domain_info, html_content)
            
            results["posts"].append({
                "domain": domain_info['domain'],
                "status": "success" if success else "failed",
                "timestamp": datetime.now().isoformat()
            })
            
        except Exception as e:
            print(f"❌ Error processing {domain_info['domain']}: {str(e)}")
            results["posts"].append({
                "domain": domain_info['domain'],
                "status": "error",
                "error": str(e)
            })
    
    # Save results log
    with open('blog_generation_log.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    print("=" * 60)
    print("✨ Blog generation complete!")
    print(f"Results saved to blog_generation_log.json")
    print("=" * 60)

if __name__ == "__main__":
    main()
