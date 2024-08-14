/ip firewall address-list remove [/ip firewall address-list find list=wg_domains]
/ip firewall address-list
:do { add address=aaa1.mytvnet.vn list=wg_domains} on-error={}
