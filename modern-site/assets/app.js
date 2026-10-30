const toggle=document.querySelector('.menu-toggle');
const nav=document.querySelector('#navigation');
function closeMenu(){nav.classList.remove('open');toggle.setAttribute('aria-expanded','false');toggle.setAttribute('aria-label','Menüyü aç');}
toggle?.addEventListener('click',()=>{const open=nav.classList.toggle('open');toggle.setAttribute('aria-expanded',String(open));toggle.setAttribute('aria-label',open?'Menüyü kapat':'Menüyü aç');});
document.addEventListener('keydown',event=>{if(event.key==='Escape')closeMenu();});
nav?.addEventListener('click',event=>{if(event.target.closest('a'))closeMenu();});
document.querySelectorAll('[data-filter]').forEach(button=>button.addEventListener('click',()=>{document.querySelectorAll('[data-filter]').forEach(item=>item.setAttribute('aria-pressed',String(item===button)));document.querySelectorAll('.catalog-grid [data-category]').forEach(card=>{card.hidden=button.dataset.filter!=='Tümü'&&card.dataset.category!==button.dataset.filter;});}));
const viewer=document.querySelector('#image-viewer');
document.querySelectorAll('.zoom-image').forEach(button=>button.addEventListener('click',()=>{const img=button.querySelector('img');const full=viewer.querySelector('img');full.src=img.src;full.alt=img.alt;viewer.querySelector('p').textContent=img.alt;viewer.showModal();}));
viewer?.querySelector('.viewer-close').addEventListener('click',()=>viewer.close());
viewer?.addEventListener('click',event=>{if(event.target===viewer){const rect=viewer.getBoundingClientRect();if(event.clientX<rect.left||event.clientX>rect.right||event.clientY<rect.top||event.clientY>rect.bottom)viewer.close();}});
