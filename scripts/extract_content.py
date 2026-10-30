import re,json,pathlib
root=pathlib.Path(__file__).resolve().parents[1]
sql=next((root/'private/database').iterdir()).read_text()
def rows(table):
 for block in re.findall(r'INSERT INTO `'+table+r'` VALUES\s*\n(.*?);\n',sql,re.S):
  for row in re.finditer(r'\((.*)\)(?:,|$)',block):
   vals=[];s=row[1];i=0
   while i<len(s):
    if s[i]=="'":
     i+=1;v=''
     while i<len(s):
      if s[i]=='\\':
       i+=1;v+= {'n':'\n','r':'\r','t':'\t','0':'\0'}.get(s[i],s[i]);i+=1
      elif s[i]=="'": i+=1;break
      else:v+=s[i];i+=1
     vals.append(v)
    else:
     end=s.find(',',i);end=len(s) if end<0 else end;vals.append(s[i:end]);i=end
    if i<len(s) and s[i]==',':i+=1
   yield vals
posts=[]
for r in rows('wp_posts'):
 if len(r)>20 and r[7]=='publish' and r[20] in ['page','post']:
  posts.append(dict(id=r[0],title=r[5],slug=r[11],content=r[4],type=r[20]))
(root/'data').mkdir(exist_ok=True)
(root/'data/content.json').write_text(json.dumps(posts,ensure_ascii=False,indent=2))
for p in posts: print(p['id'],p['type'],p['slug'],p['title'],len(p['content']))
