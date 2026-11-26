const root=document.body;
let currentLang=localStorage.getItem("gsslLang")||"en";
const langButtons=document.querySelectorAll(".lang");
const menuBtn=document.querySelector(".menu-btn");
const navWrap=document.querySelector(".nav-wrap");

function applyLanguage(lang){
  currentLang=lang;
  localStorage.setItem("gsslLang",lang);
  root.classList.toggle("bn",lang==="bn");
  document.documentElement.lang=lang;
  document.querySelectorAll("[data-en]").forEach(el=>{
    const value=el.getAttribute(`data-${lang}`);
    if(value!==null) el.innerHTML=value;
  });
  document.querySelectorAll("[data-placeholder-en]").forEach(el=>{
    const value=el.getAttribute(`data-placeholder-${lang}`);
    if(value!==null) el.placeholder=value;
  });
  langButtons.forEach(b=>b.classList.toggle("active",b.dataset.lang===lang));
  document.querySelectorAll("select option[data-en]").forEach(opt=>{
    opt.textContent=opt.getAttribute(`data-${lang}`)||opt.getAttribute("data-en");
  });
}
langButtons.forEach(btn=>btn.addEventListener("click",()=>applyLanguage(btn.dataset.lang)));
menuBtn?.addEventListener("click",()=>navWrap.classList.toggle("open"));
document.querySelectorAll(".nav a").forEach(a=>a.addEventListener("click",()=>navWrap.classList.remove("open")));
applyLanguage(currentLang);
