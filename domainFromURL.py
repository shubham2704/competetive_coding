def domain_name(url):
    st = url.replace("http://", "")
    tt = st.replace("https://","")
    ut = tt.replace("www.","")  
    s = ut.split(".")
    return s[0]

print(domain_name("http://github.com/carbonfive/raygun"))