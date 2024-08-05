import requests

# Danh sách các domain và subdomain cần tìm
domains = [
    'mytv.vn',
    '*.mytv.vn',
    'vnptmedia.vn',
    '*.vnptmedia.vn',
    'mytv.net.vn',
    '*.mytv.net.vn',
    'mytv.com.vn',
    '*.mytv.com.vn',
    'vnpt.vn',
    '*.vnpt.vn'
]

# Hàm kiểm tra domain và subdomain
def matches_domain(url, domain):
    if domain.startswith('*.'):
        domain = domain[2:]
        return url.endswith(domain) and not url == domain
    return url == domain

# Tải file url.log
response = requests.get('https://duchoa.biz/uploads/uploads/url.log')
urls = response.text.splitlines()

# Lọc domain
filtered_domains = set()
for url in urls:
    for domain in domains:
        if matches_domain(url, domain):
            filtered_domains.add(url)
            break

# Đường dẫn tới file filtered_domains.txt
output_file = 'filtered_domains.txt'

# Ghi kết quả vào file
with open(output_file, 'w') as f:
    for domain in filtered_domains:
        f.write(f"{domain}\n")

print(f"Filtered domains have been written to {output_file}")
