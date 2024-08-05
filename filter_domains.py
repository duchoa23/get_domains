import requests
import fnmatch

# Danh sách các domain và subdomain cần so sánh, bao gồm wildcard
allowed_domains = [
    'mytv.vn', '*.mytv.vn',
    'mytvnet.vn', '*.mytvnet.vn',
    'vnptmedia.vn', '*.vnptmedia.vn',
    'mytv.net.vn', '*.mytv.net.vn',
    'mytv.com.vn', '*.mytv.com.vn',
    'vnpt.vn', '*.vnpt.vn'
]

# Đọc file log từ URL
url = 'https://duchoa.biz/uploads/uploads/url.log'
response = requests.get(url)
data = response.text

# Tách dữ liệu theo dòng và sau đó theo dấu phẩy
lines = data.splitlines()
domains = [line.split(',')[-1] for line in lines]

# Xử lý từng domain để loại bỏ phần sau dấu '/'
cleaned_domains = [domain.split('/')[0] for domain in domains]

# Hàm kiểm tra nếu domain thỏa mãn danh sách cho phép với wildcard
def is_allowed(domain, allowed_domains):
    return any(fnmatch.fnmatch(domain, pattern) for pattern in allowed_domains)

# Lọc các domain theo danh sách cho phép và loại bỏ trùng lặp
filtered_domains = set(domain for domain in cleaned_domains if is_allowed(domain, allowed_domains))

# Lưu danh sách domain đã lọc vào file 'domain.txt'
with open('domain.txt', 'w') as file:
    for domain in sorted(filtered_domains):  # Sắp xếp danh sách nếu cần
        file.write(f"{domain}\n")

print("Danh sách domain đã lọc và lưu vào 'domain.txt'.")
