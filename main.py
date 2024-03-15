import re
with open("Input.txt")as file:
  text=file.read()
quotes=re.findall(r"(Topic URL:.*?)(?=\nTopic URL:|\Z)",text,re.DOTALL)
with open("Output.txt","w")as file:
  for quote in quotes:
    quote=re.sub(r"\b(?:plaintext|Copy code)\b.*\n","",quote)
    url=re.search(r"Topic URL:(.*)",quote).group(1).strip()if re.search(r"Topic URL:(.*)",quote)else None
    title=re.search(r"Topic title:(.*)",quote).group(1).strip()if re.search(r"Topic title:(.*)",quote)else None
    keywords=re.search(r"Keywords:(.*)",quote).group(1).strip().lower().replace(",",", ")if re.search(r"Keywords:(.*)",quote)else "none"
    file.write("[quote][big][b][url=" + url + "]" + title + "[/url][/b][/big]\n")
    file.write("[b]Keywords:[/b] " + keywords + "[/quote]\n")
print("Written")