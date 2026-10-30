from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
root=Path(__file__).resolve().parents[1]/'modern-site'
class Document(HTMLParser):
 def __init__(self):super().__init__();self.links=[];self.ids=set();self.h1=0
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.add(a['id'])
  if tag=='h1':self.h1+=1
  for key in ['src','href']:
   if a.get(key):self.links.append(a[key])
docs={}
for f in root.rglob('*.html'):
 d=Document();d.feed(f.read_text());docs[f]=d
errors=[];checked=0
for f,d in docs.items():
 if d.h1!=1:errors.append(f'{f}: {d.h1} h1 elements')
 if '[vc_' in f.read_text():errors.append(f'{f}: unconverted WordPress shortcode')
 for u in d.links:
  p=urlsplit(u)
  if p.scheme or p.netloc:continue
  target=root/unquote(p.path).lstrip('/') if p.path.startswith('/') else f.parent/unquote(p.path)
  if not p.path:target=f
  if target.is_dir():target=target/'index.html'
  checked+=1
  if not target.exists():errors.append(f'{f.relative_to(root)}: missing {u}')
  elif p.fragment and target in docs and p.fragment not in docs[target].ids:errors.append(f'{f.relative_to(root)}: missing anchor {u}')
for f in root.rglob('*'):
 if f.is_file() and f.suffix.lower() not in ['.html','.css','.js','.jpg','.jpeg','.png','.gif','.pdf','.webp','.woff2','.txt','.xml',''] and f.name!='.htaccess':errors.append(f'Unexpected public file: {f}')
print(f'{len(docs)} pages; {checked} internal links/assets/anchors checked.')
if errors:print('\n'.join(errors));raise SystemExit(1)
print('PASS: all internal targets exist; no WordPress shortcodes or private source files in public output.')
