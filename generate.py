#!/usr/bin/env python3
"""Site generator for diysignguy.com — edit content below, run to rebuild all pages."""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

STYLE = """
  :root{--ink:#141a22;--ink-2:#1d2530;--ink-3:#28313f;--paper:#f5f6f8;--white:#fff;
    --amber:#ffb420;--amber-deep:#e69500;--amber-text:#8f5500;--glow:rgba(255,180,32,.35);--line:#e2e6ec;
    --muted:#5b6675;--muted-dark:#9aa6b5;--radius:14px;}
  .skip{position:absolute;left:-9999px;top:0;background:var(--amber);color:var(--ink);padding:12px 20px;font-weight:700;z-index:100;border-radius:0 0 10px 0;text-decoration:none;}
  .skip:focus{left:0;}
  a:focus-visible,button:focus-visible,input:focus-visible,select:focus-visible,textarea:focus-visible,summary:focus-visible{outline:3px solid var(--amber-deep);outline-offset:2px;}
  @media(prefers-reduced-motion:reduce){*,*::before,*::after{animation:none !important;transition:none !important;}html{scroll-behavior:auto;}}
  *{margin:0;padding:0;box-sizing:border-box;}
  html{scroll-behavior:smooth;}
  body{font-family:'Segoe UI',system-ui,-apple-system,Arial,sans-serif;color:var(--ink);background:var(--white);line-height:1.6;}
  img{max-width:100%;display:block;} a{color:inherit;}
  .wrap{max-width:1120px;margin:0 auto;padding:0 24px;}
  h1,h2,h3{line-height:1.15;font-weight:800;letter-spacing:-.01em;}
  section{padding:68px 0;}
  .kicker{display:inline-block;font-size:.78rem;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--amber-text);margin-bottom:14px;}
  .hero .kicker,.page-hero .kicker,.kit-dark .kicker,.cta-band .kicker{color:var(--amber);}
  .sec-title{font-size:clamp(1.6rem,3.2vw,2.3rem);margin-bottom:14px;}
  .sec-sub{color:var(--muted);max-width:660px;font-size:1.05rem;}
  header{position:sticky;top:0;z-index:50;background:var(--ink);color:#fff;box-shadow:0 2px 14px rgba(0,0,0,.25);}
  .nav{display:flex;align-items:center;justify-content:space-between;height:68px;}
  .brand{display:flex;align-items:center;gap:12px;font-weight:800;font-size:1.1rem;letter-spacing:.02em;text-decoration:none;}
  .brand .logo-box{width:42px;height:42px;border-radius:9px;background:linear-gradient(160deg,var(--amber),var(--amber-deep));display:flex;align-items:center;justify-content:center;color:var(--ink);font-size:.55rem;font-weight:800;text-align:center;line-height:1.1;box-shadow:0 0 18px var(--glow);}
  .brand span em{color:var(--amber);font-style:normal;}
  .nav-links{display:flex;gap:24px;align-items:center;font-size:.92rem;}
  .nav-links a{text-decoration:none;color:#cdd5e0;font-weight:600;}
  .nav-links a:hover,.nav-links a.active{color:var(--amber);}
  .nav-links a.btn-amber,.nav-links a.btn-amber:hover{color:var(--ink);}
  .btn{display:inline-block;padding:13px 26px;border-radius:10px;font-weight:700;text-decoration:none;font-size:.95rem;transition:transform .15s,box-shadow .15s;cursor:pointer;border:none;}
  .btn-amber{background:linear-gradient(160deg,var(--amber),var(--amber-deep));color:var(--ink);box-shadow:0 4px 18px var(--glow);}
  .btn-amber:hover{transform:translateY(-2px);box-shadow:0 8px 26px var(--glow);}
  .btn-ghost{border:2px solid #ffffff44;color:#fff;}
  .btn-sm{padding:10px 18px;font-size:.88rem;}
  .hero{background:radial-gradient(1100px 520px at 75% -10%,#33405288 0%,transparent 60%),var(--ink);color:#fff;padding:84px 0 80px;}
  .hero-grid{display:grid;grid-template-columns:1.15fr .85fr;gap:56px;align-items:center;}
  .hero h1{font-size:clamp(2rem,4.4vw,3.1rem);margin-bottom:20px;}
  .lit{color:var(--amber);text-shadow:0 0 26px var(--glow);}
  .hero p.lead{font-size:1.13rem;color:#c3ccd9;margin-bottom:28px;max-width:540px;}
  .hero-ctas{display:flex;gap:14px;flex-wrap:wrap;margin-bottom:32px;}
  .hero-stats{display:flex;gap:34px;flex-wrap:wrap;}
  .hero-stats .stat b{display:block;font-size:1.5rem;color:var(--amber);}
  .hero-stats .stat span{font-size:.85rem;color:var(--muted-dark);}
  .page-hero{background:radial-gradient(900px 420px at 80% -20%,#33405288 0%,transparent 60%),var(--ink);color:#fff;padding:64px 0 58px;}
  .page-hero h1{font-size:clamp(1.9rem,3.8vw,2.7rem);margin-bottom:14px;}
  .page-hero p{color:#c3ccd9;max-width:640px;font-size:1.08rem;}
  .photo-ph{background:var(--ink-2);border:2px dashed #46536566;border-radius:var(--radius);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;color:var(--muted-dark);text-align:center;padding:20px;font-size:.85rem;}
  .photo-ph .ph-icon{font-size:2rem;opacity:.7;}
  .hero .photo-ph{min-height:360px;box-shadow:0 20px 50px rgba(0,0,0,.35);}
  .photo-ph.light{background:#eef1f5;border-color:#c6cdd8;color:#4d5866;}
  .ph-img{width:100%;display:block;object-fit:cover;}
  .hero-img-wrap{border-radius:var(--radius);overflow:hidden;box-shadow:0 20px 50px rgba(0,0,0,.35);}
  .card-img{height:230px;border-bottom:1px solid var(--line);}
  .round-img{border-radius:var(--radius);max-height:480px;box-shadow:0 14px 38px rgba(20,26,34,.15);}
  .post-img{height:170px;border-bottom:1px solid var(--line);}
  .trust{background:var(--amber);}
  .trust .wrap{display:grid;grid-template-columns:repeat(4,1fr);}
  .trust .t-item{padding:18px 10px;text-align:center;font-weight:700;color:var(--ink);font-size:.92rem;}
  .trust .t-item small{display:block;font-weight:600;font-size:.78rem;opacity:.75;}
  .alt{background:var(--paper);}
  .steps{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;margin-top:44px;}
  .step{background:#fff;border:1px solid var(--line);border-radius:var(--radius);padding:26px 22px;}
  .step .num{width:38px;height:38px;border-radius:50%;background:var(--ink);color:var(--amber);display:flex;align-items:center;justify-content:center;font-weight:800;margin-bottom:16px;}
  .step h3{font-size:1.05rem;margin-bottom:8px;}
  .step p{font-size:.92rem;color:var(--muted);}
  .about-grid{display:grid;grid-template-columns:.9fr 1.1fr;gap:56px;align-items:center;}
  .about-grid .photo-ph{min-height:400px;}
  .about-copy p{color:var(--muted);margin-bottom:16px;font-size:1.02rem;}
  .about-copy p b{color:var(--ink);}
  .prod-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:44px;}
  .prod-card-wrap{position:relative;}
  .prod{border:1px solid var(--line);border-radius:var(--radius);overflow:hidden;background:#fff;display:flex;flex-direction:column;transition:box-shadow .2s,transform .2s;height:100%;}
  .prod:hover{box-shadow:0 14px 38px rgba(20,26,34,.12);transform:translateY(-3px);}
  .prod .photo-ph{min-height:200px;border-radius:0;border:none;border-bottom:1px solid var(--line);}
  .prod-body{padding:26px 24px 28px;display:flex;flex-direction:column;flex:1;}
  .prod .size{font-size:1.9rem;font-weight:800;}
  .prod .size small{font-size:.95rem;color:var(--muted);font-weight:600;}
  .prod .use{margin:6px 0 14px;font-weight:700;color:var(--amber-text);font-size:.88rem;text-transform:uppercase;letter-spacing:.06em;}
  .prod p{font-size:.93rem;color:var(--muted);margin-bottom:18px;flex:1;}
  .badge{position:absolute;z-index:2;background:var(--ink);color:var(--amber);font-size:.72rem;font-weight:800;letter-spacing:.08em;text-transform:uppercase;padding:6px 12px;border-radius:999px;margin:14px;box-shadow:0 4px 12px rgba(0,0,0,.25);}
  .kit-dark{background:var(--ink);color:#fff;}
  .kit-dark .sec-sub{color:var(--muted-dark);}
  .kit-grid{display:grid;grid-template-columns:.95fr 1.05fr;gap:56px;align-items:center;margin-top:20px;}
  .kit-list{list-style:none;margin-top:26px;display:grid;gap:14px;}
  .kit-list li{display:flex;gap:14px;align-items:flex-start;background:var(--ink-2);border:1px solid #38445533;border-radius:12px;padding:15px 18px;}
  .kit-list .chk{color:var(--amber);font-weight:800;}
  .kit-list b{display:block;font-size:.97rem;}
  .kit-list span{font-size:.88rem;color:var(--muted-dark);}
  .kit-grid .photo-ph{min-height:400px;}
  .video-ph{background:var(--ink-2);border:2px dashed #46536566;border-radius:var(--radius);min-height:420px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px;color:var(--muted-dark);text-align:center;padding:30px;margin-top:40px;}
  .video-ph .play{width:74px;height:74px;border-radius:50%;background:linear-gradient(160deg,var(--amber),var(--amber-deep));display:flex;align-items:center;justify-content:center;font-size:1.6rem;color:var(--ink);box-shadow:0 0 30px var(--glow);}
  .blog-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:40px;}
  .post-card{border:1px solid var(--line);border-radius:var(--radius);background:#fff;overflow:hidden;display:flex;flex-direction:column;text-decoration:none;transition:box-shadow .2s,transform .2s;}
  a.post-card:hover{box-shadow:0 14px 38px rgba(20,26,34,.12);transform:translateY(-3px);}
  .post-card .photo-ph{min-height:150px;border-radius:0;border:none;border-bottom:1px solid var(--line);}
  .post-body{padding:22px;}
  .post-body .tag{display:inline-block;font-size:.7rem;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--amber-text);margin-bottom:8px;}
  .post-body h3{font-size:1.05rem;margin-bottom:8px;}
  .post-body p{font-size:.88rem;color:var(--muted);}
  .soon{opacity:.65;} .soon .tag{color:var(--muted);}
  .who-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;margin-top:40px;}
  .who-card{background:#fff;border:1px solid var(--line);border-radius:var(--radius);padding:24px 22px;}
  .who-card .ic{font-size:1.6rem;margin-bottom:10px;}
  .who-card h3{font-size:1rem;margin-bottom:6px;}
  .who-card p{font-size:.88rem;color:var(--muted);}
  .cta-band{background:var(--ink);color:#fff;padding:52px 0;}
  .cta-band .wrap{display:flex;align-items:center;justify-content:space-between;gap:30px;flex-wrap:wrap;}
  .cta-band .big{font-size:clamp(1.3rem,2.4vw,1.7rem);font-weight:800;max-width:620px;}
  .cta-band .big em{color:var(--amber);font-style:normal;}
  .quote-grid{display:grid;grid-template-columns:.85fr 1.15fr;gap:56px;align-items:start;}
  .quote-info p{color:var(--muted);margin-bottom:22px;}
  .assure{display:grid;gap:12px;margin-top:26px;}
  .assure div{display:flex;gap:10px;font-size:.92rem;}
  .assure .chk{color:var(--amber-text);font-weight:800;}
  form.qform{background:var(--paper);border:1px solid var(--line);border-radius:var(--radius);padding:34px;display:grid;gap:18px;}
  .frow{display:grid;grid-template-columns:1fr 1fr;gap:18px;}
  .field label{display:block;font-size:.82rem;font-weight:700;margin-bottom:6px;}
  .field input,.field select,.field textarea{width:100%;padding:12px 14px;border:1px solid #cfd6df;border-radius:9px;font-size:.95rem;font-family:inherit;background:#fff;color:var(--ink);}
  .field input:focus,.field select:focus,.field textarea:focus{outline:2px solid var(--amber);border-color:var(--amber);}
  .field textarea{min-height:110px;resize:vertical;}
  .qform .btn{width:100%;font-size:1.05rem;padding:15px;}
  .qform .fine{font-size:.78rem;color:var(--muted);text-align:center;}
  .faq-list{margin-top:36px;display:grid;gap:14px;max-width:860px;}
  details{background:#fff;border:1px solid var(--line);border-radius:12px;padding:20px 24px;}
  details summary{font-weight:700;cursor:pointer;font-size:1rem;list-style:none;display:flex;justify-content:space-between;align-items:center;gap:16px;}
  details summary::after{content:"+";font-size:1.3rem;color:var(--amber-text);font-weight:800;}
  details[open] summary::after{content:"\\2013";}
  details p{margin-top:12px;color:var(--muted);font-size:.94rem;}
  article.post{max-width:760px;margin:0 auto;}
  article.post h1{font-size:clamp(1.8rem,3.4vw,2.5rem);margin-bottom:18px;}
  article.post h2{font-size:1.4rem;margin:34px 0 12px;}
  article.post p{color:#333c48;margin-bottom:16px;font-size:1.03rem;}
  article.post ul{margin:0 0 16px 22px;color:#333c48;}
  article.post li{margin-bottom:8px;}
  .post-meta{color:var(--muted);font-size:.88rem;margin-bottom:26px;}
  footer{background:var(--ink);color:var(--muted-dark);padding:54px 0 30px;font-size:.9rem;}
  .foot-grid{display:grid;grid-template-columns:1.4fr 1fr 1fr 1fr;gap:36px;margin-bottom:38px;}
  footer h2{color:#fff;font-size:.95rem;margin-bottom:14px;font-weight:800;}
  footer a{color:var(--muted-dark);text-decoration:none;display:block;margin-bottom:8px;}
  footer a:hover{color:var(--amber);}
  .soc-row{display:flex;gap:10px;margin-top:16px;}
  .soc{width:38px;height:38px;border-radius:50%;background:var(--ink-2);border:1px solid #38445566;display:flex !important;align-items:center;justify-content:center;font-weight:800;font-size:.8rem;color:#cdd5e0 !important;text-decoration:none;margin:0 !important;}
  .soc:hover{background:var(--amber);color:var(--ink) !important;border-color:var(--amber);}
  .foot-bottom{border-top:1px solid #333e4d55;padding-top:22px;display:flex;justify-content:space-between;flex-wrap:wrap;gap:10px;font-size:.8rem;}
  @media(max-width:900px){
    .hero-grid,.kit-grid,.quote-grid,.about-grid{grid-template-columns:1fr;}
    .steps,.who-grid{grid-template-columns:repeat(2,1fr);}
    .prod-grid,.blog-grid{grid-template-columns:1fr;}
    .trust .wrap{grid-template-columns:repeat(2,1fr);}
    .nav-links{display:none;}
    .foot-grid{grid-template-columns:1fr;}
    .hero .photo-ph{min-height:240px;}
  }
"""

SOCIALS = """
        <div class="soc-row">
          <a class="soc" href="#" title="Facebook" aria-label="Facebook">f</a>
          <a class="soc" href="#" title="Instagram" aria-label="Instagram">IG</a>
          <a class="soc" href="#" title="TikTok" aria-label="TikTok">TT</a>
          <a class="soc" href="#" title="YouTube" aria-label="YouTube">YT</a>
        </div>"""

def header(active, root=""):
    def cls(name):
        return ' class="active"' if active == name else ''
    return f"""
<header>
  <div class="wrap nav">
    <a class="brand" href="{root}index.html">
      <div class="logo-box">YOUR<br>LOGO</div>
      <span>DIY <em>SIGN</em> GUY</span>
    </a>
    <nav class="nav-links">
      <a href="{root}index.html"{cls('home')}>Home</a>
      <a href="{root}kits.html"{cls('kits')}>Our Kits</a>
      <a href="{root}pylon-signs.html"{cls('pylon')}>Pylon Pole Signs</a>
      <a href="{root}faq.html"{cls('faq')}>Q &amp; A</a>
      <a href="{root}contact.html"{cls('contact')}>Contact</a>
      <a href="{root}contact.html" class="btn btn-amber btn-sm">Get a Free Quote</a>
    </nav>
  </div>
</header>"""

def cta_band(root=""):
    return f"""
<div class="cta-band">
  <div class="wrap">
    <div class="big">Ready to see your price? Every sign is cut to order — tell us your size and save <em>up to 60%</em> over local retail.</div>
    <a href="{root}contact.html" class="btn btn-amber">Contact Now for a Quote</a>
  </div>
</div>"""

def footer(root=""):
    return f"""
<footer>
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <h2>DIY SIGN GUY</h2>
        <p style="max-width:300px;">Pre-lit aluminum sign cabinet kits, custom cut to your size and shipped nationwide. 20+ years in the sign business.</p>
        {SOCIALS}
      </div>
      <div>
        <h2>Our Kits</h2>
        <a href="{root}kits.html">4" Wall Mount Cabinet</a>
        <a href="{root}kits.html">7" Wall / Double-Pole Cabinet</a>
        <a href="{root}kits.html">10" Pylon / Single-Pole Cabinet</a>
      </div>
      <div>
        <h2>Learn</h2>
        <a href="{root}pylon-signs.html">Pylon Pole Signs</a>
        <a href="{root}faq.html">Questions &amp; Answers</a>
        <a href="{root}blog/which-sign-cabinet-do-i-need.html">Which Cabinet Do I Need?</a>
      </div>
      <div>
        <h2>Get Started</h2>
        <a href="{root}contact.html">Request a Free Quote</a>
        <a href="{root}kits.html">Shop Our Kits</a>
      </div>
    </div>
    <div class="foot-bottom">
      <div>&copy; 2026 DIY Sign Guy &middot; diysignguy.com</div>
      <div><a href="{root}privacy.html" style="display:inline;margin:0 14px 0 0;">Privacy Policy</a><a href="{root}terms.html" style="display:inline;margin:0;">Terms of Use</a></div>
      <div>Build It. Light It. Own It.</div>
    </div>
  </div>
</footer>"""

def page(filename, title, desc, active, content, root=""):
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<style>{STYLE}</style>
</head>
<body>
<a class="skip" href="#main">Skip to main content</a>
{header(active, root)}
<main id="main">
{content}
</main>
{cta_band(root)}
{footer(root)}
</body>
</html>"""
    path = os.path.join(ROOT, filename)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(html)
    print("wrote", filename)

QUOTE_FORM = """
    <form class="qform" action="https://formsubmit.co/fortunefivesignco@gmail.com" method="POST">
      <input type="hidden" name="_subject" value="New Quote Request — diysignguy.com">
      <input type="hidden" name="_captcha" value="false">
      <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off" aria-hidden="true">
      <div class="frow">
        <div class="field"><label for="q-name">Your Name *</label><input id="q-name" type="text" name="name" required placeholder="John Smith" autocomplete="name"></div>
        <div class="field"><label for="q-business">Business Name</label><input id="q-business" type="text" name="business" placeholder="Smith Hardware" autocomplete="organization"></div>
      </div>
      <div class="frow">
        <div class="field"><label for="q-email">Email *</label><input id="q-email" type="email" name="email" required placeholder="you@email.com" autocomplete="email"></div>
        <div class="field"><label for="q-phone">Phone</label><input id="q-phone" type="tel" name="phone" placeholder="(555) 555-5555" autocomplete="tel"></div>
      </div>
      <div class="frow">
        <div class="field"><label for="q-cabinet">Cabinet Size</label>
          <select id="q-cabinet" name="cabinet">
            <option value="">Not sure — help me choose</option>
            <option>4" — Wall Mount (Best Seller)</option>
            <option>7" — Wall or Double-Pole</option>
            <option>10" — Pylon / Single-Pole</option>
          </select>
        </div>
        <div class="field"><label for="q-dimensions">Sign Dimensions</label><input id="q-dimensions" type="text" name="dimensions" placeholder="e.g., 3' tall x 6' wide"></div>
      </div>
      <div class="frow">
        <div class="field"><label for="q-mount">How Will It Mount?</label>
          <select id="q-mount" name="mount">
            <option value="">Select one</option>
            <option>Flat on a wall</option>
            <option>Post &amp; panel</option>
            <option>Double pole</option>
            <option>Single pole / pylon</option>
            <option>Not sure yet</option>
          </select>
        </div>
        <div class="field"><label for="q-zip">Shipping ZIP Code</label><input id="q-zip" type="text" name="zip" placeholder="e.g., 75201" autocomplete="postal-code"></div>
      </div>
      <div class="field"><label for="q-details">Anything Else We Should Know?</label><textarea id="q-details" name="details" placeholder="Single or double sided, timeline, questions — whatever helps us quote it right."></textarea></div>
      <button type="submit" class="btn btn-amber">Send My Quote Request</button>
      <div class="fine">We typically respond within one business day.</div>
    </form>"""

# ---------------- HOME ----------------
HOME = """
<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <span class="kicker">Pre-Lit Aluminum Sign Cabinet Kits &middot; Shipped Nationwide</span>
      <h1>A Professional <span class="lit">Lighted Sign</span> for Your Business — Built by Us, Installed by You.</h1>
      <p class="lead">We custom-cut heavy-duty aluminum sign cabinets to your exact size, weld the corners, install edge-lit LEDs, and ship the complete kit to your door — power supply included. You put it up and save up to 60% over local retail.</p>
      <div class="hero-ctas">
        <a href="contact.html" class="btn btn-amber">Get My Free Quote</a>
        <a href="kits.html" class="btn btn-ghost">See Our Kits</a>
      </div>
      <div class="hero-stats">
        <div class="stat"><b>2004</b><span>Helping DIYers ever since</span></div>
        <div class="stat"><b>60%</b><span>Savings vs. local retail</span></div>
        <div class="stat"><b>3</b><span>Cabinet sizes: 4", 7", 10"</span></div>
      </div>
    </div>
    <div class="hero-img-wrap"><img class="ph-img" src="images/hero-collage.jpg" alt="DIY Sign Guy — your one-stop shop for outdoor LED lighted sign kits and cabinets since 2004, shown on a small-town main street at dusk with lighted wall, kit, and pylon signs"></div>
  </div>
</section>

<div class="trust">
  <div class="wrap">
    <div class="t-item">Welded Corners<small>Not screwed-together frames</small></div>
    <div class="t-item">Pre-Lit LEDs Inside<small>Edge-lit, power supply included</small></div>
    <div class="t-item">Cut to Your Size<small>Every kit made to order</small></div>
    <div class="t-item">Ships Nationwide<small>Packed in 4&ndash;6 pieces</small></div>
  </div>
</div>

<section>
  <div class="wrap about-grid">
    <img class="ph-img round-img" src="images/meet-the-sign-guy.jpg" alt="Dean, the DIY Sign Guy, in his shop holding a Made-in-USA aluminum sign extrusion — Built by You, Backed by Me">
    <div class="about-copy">
      <span class="kicker">Meet the Sign Guy</span>
      <h2 class="sec-title">20+ Years of Building Signs. One Simple Idea.</h2>
      <p>I've spent 20+ years in the sign business, and in that time I've watched too many small business owners walk away from a lighted sign because of the price tag — not the sign, the <b>markup</b>.</p>
      <p>Here's the truth: when you buy from a local sign company, you're paying for their showroom, their salespeople, and their install crew. The sign itself is the smallest part of the bill.</p>
      <p>So I do it differently. <b>I build your sign cabinet in my shop</b> — cut from 26-foot sticks of extruded aluminum, corners welded by hand, LEDs and power supply fitted to your exact size — and ship the complete kit straight to you. You handle the install, and you keep the difference. That's usually <b>up to 60% off local retail</b>.</p>
      <p>No showroom. No sales office. Just a guy who's been building signs for two decades, and a better way for you to get one.</p>
      <a href="kits.html" class="btn btn-amber" style="margin-top:8px;">See How Our Kits Work</a>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <span class="kicker">What We Offer</span>
    <h2 class="sec-title">Three Cabinet Depths. Every Size You Need.</h2>
    <p class="sec-sub">All three are the same heavy-duty extruded aluminum, welded corners, and Pre-Lit LED system — the difference is depth and how you plan to mount it.</p>
    <div class="prod-grid">
      <div class="prod-card-wrap">
        <span class="badge">&#9733; Best Seller</span>
        <div class="prod">
          <img class="ph-img card-img" src="images/storefront-cabinet-blank.jpg" alt="Blank LED-lighted sign cabinet glowing on a brick storefront at night, ready for graphics">
          <div class="prod-body">
            <div class="size">4" <small>Wide Cabinet</small></div>
            <div class="use">Wall Mount</div>
            <p>Our most popular kit. A clean, low-profile lighted sign that mounts flat to your building — perfect for storefronts, offices, and retail strips.</p>
            <a href="kits.html" class="btn btn-amber btn-sm">Learn More</a>
          </div>
        </div>
      </div>
      <div class="prod-card-wrap">
        <div class="prod">
          <img class="ph-img card-img" src="images/completed-cabinet-wild-peak.jpg" alt="Completed DIY Sign Guy lighted cabinet with an installed graphics face, lit up and glowing">
          <div class="prod-body">
            <div class="size">7" <small>Wide Cabinet</small></div>
            <div class="use">Wall Mount &middot; Double-Pole</div>
            <p>The versatile middle weight. Deep enough for double-pole and post-and-panel installs, still clean on a wall.</p>
            <a href="kits.html" class="btn btn-amber btn-sm">Learn More</a>
          </div>
        </div>
      </div>
      <div class="prod-card-wrap">
        <div class="prod">
          <img class="ph-img card-img" src="images/pylon-signs-group.jpg" alt="Five outdoor LED pylon pole signs lit at dusk in front of a general store, showing different sizes and colors">
          <div class="prod-body">
            <div class="size">10" <small>Wide Cabinet</small></div>
            <div class="use">Pylon &middot; Single-Pole</div>
            <p>Our heavy-duty cabinet built for pylon and single-pole signs — big, high-visibility signs you see from the road.</p>
            <a href="pylon-signs.html" class="btn btn-amber btn-sm">Learn More</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <span class="kicker">How It Works</span>
    <h2 class="sec-title">From Our Shop to Your Wall in Four Steps</h2>
    <div class="steps">
      <div class="step"><div class="num">1</div><h3>Tell Us Your Size</h3><p>Send us your dimensions and where the sign is going: wall, posts, or pylon pole.</p></div>
      <div class="step"><div class="num">2</div><h3>We Build Your Kit</h3><p>Cut from 26-foot aluminum sticks, corners welded, edge-lit LEDs fitted to your sign.</p></div>
      <div class="step"><div class="num">3</div><h3>It Ships to Your Door</h3><p>Arrives in 4&ndash;6 pieces sized for safe shipping, with the right 12V power supply included.</p></div>
      <div class="step"><div class="num">4</div><h3>You Install &amp; Light It Up</h3><p>Assemble the pre-fit pieces, mount it, plug it in. A professional sign at a DIY price.</p></div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <span class="kicker">From the Shop</span>
    <h2 class="sec-title">Sign Advice From 23 Years in the Business</h2>
    <p class="sec-sub">Straight answers on choosing, buying, and installing your own business sign.</p>
    <div class="blog-grid">
      <a class="post-card" href="blog/which-sign-cabinet-do-i-need.html">
        <img class="ph-img post-img" src="images/diy-sign-kits-overview.jpg" alt="DIY Sign Kits overview — wall sign kits, pole and pylon sign kits, everything you need in one kit">
        <div class="post-body">
          <span class="tag">Buying Guide</span>
          <h3>Which Sign Cabinet Do I Need — 4", 7", or 10"?</h3>
          <p>The simple rule of thumb we use to match every customer to the right cabinet, based on where the sign is going.</p>
        </div>
      </a>
      <div class="post-card soon">
        <img class="ph-img post-img" src="images/completed-lighted-cabinets.jpg" alt="Four completed outdoor LED lighted sign cabinets with graphics for different businesses, displayed at dusk">
        <div class="post-body">
          <span class="tag">Coming Soon</span>
          <h3>How Much Does a Lighted Business Sign Really Cost?</h3>
          <p>What local sign shops charge, where that money actually goes, and how the DIY kit math works out.</p>
        </div>
      </div>
      <div class="post-card soon">
        <img class="ph-img post-img" src="images/pylon-sign-kit.jpg" alt="DIY single pole pylon sign kit with features list — shipped nationwide, offered in kit or complete">
        <div class="post-body">
          <span class="tag">Coming Soon</span>
          <h3>DIY Sign Installation: What to Expect for Each Mount Type</h3>
          <p>Wall mount, post &amp; panel, double pole, and pylon — what each install involves before you order.</p>
        </div>
      </div>
    </div>
  </div>
</section>
"""

# ---------------- KITS ----------------
KITS = """
<section class="page-hero">
  <div class="wrap">
    <span class="kicker">Our Shop Kits</span>
    <h1>Pre-Lit Sign Cabinet Kits, <span class="lit">Cut to Your Size</span></h1>
    <p>Every kit is made to order in our shop: aluminum cabinet cut from 26-foot extrusion sticks, corners welded, edge-lit LEDs installed, and the correct 12V power supply in the box. Pick your depth, tell us your size, and we build it. Rather have it built for you? Completed, graphics-ready cabinets are available too — and expert coaching comes free with every kit, before and after you buy.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <span class="kicker">The Lineup</span>
    <h2 class="sec-title">Three Cabinets. Three Ways to Mount.</h2>
    <p class="sec-sub">Same construction and Pre-Lit LED system across the board — choose your depth by how the sign will be installed.</p>
    <div class="prod-grid">
      <div class="prod-card-wrap">
        <span class="badge">&#9733; Best Seller</span>
        <div class="prod">
          <img class="ph-img card-img" src="images/storefront-cabinet-blank.jpg" alt="Blank LED-lighted sign cabinet glowing on a brick storefront at night, ready for graphics">
          <div class="prod-body">
            <div class="size">4" <small>Wide Cabinet</small></div>
            <div class="use">Wall Mount</div>
            <p>Our hottest seller. The 4" cabinet sits clean and low-profile flat against your building — the classic lighted storefront sign. If your sign is going on a wall, this is usually the one.</p>
            <a href="contact.html" class="btn btn-amber btn-sm">Quote a 4" Kit</a>
          </div>
        </div>
      </div>
      <div class="prod-card-wrap">
        <div class="prod">
          <img class="ph-img card-img" src="images/completed-cabinet-wild-peak.jpg" alt="Completed DIY Sign Guy lighted cabinet with an installed graphics face, lit up and glowing">
          <div class="prod-body">
            <div class="size">7" <small>Wide Cabinet</small></div>
            <div class="use">Wall Mount &middot; Double-Pole</div>
            <p>The versatile middle weight. Works flat on a wall like the 4", but with the depth for double-pole and post-and-panel installs — a favorite for offices, developments, and properties with a setback from the road.</p>
            <a href="contact.html" class="btn btn-amber btn-sm">Quote a 7" Kit</a>
          </div>
        </div>
      </div>
      <div class="prod-card-wrap">
        <div class="prod">
          <img class="ph-img card-img" src="images/pylon-signs-group.jpg" alt="Five outdoor LED pylon pole signs lit at dusk in front of a general store, showing different sizes and colors">
          <div class="prod-body">
            <div class="size">10" <small>Wide Cabinet</small></div>
            <div class="use">Pylon &middot; Single-Pole</div>
            <p>Our heavy-duty cabinet, designed for pylon and single-pole mounting — the big, high-visibility signs you see from the road. Different install expectations than a wall sign, so read up before you order.</p>
            <a href="pylon-signs.html" class="btn btn-amber btn-sm">About Pylon Signs</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="kit-dark">
  <div class="wrap">
    <span class="kicker">What's in the Box</span>
    <h2 class="sec-title" style="color:#fff;">Every Kit Arrives Ready to Assemble</h2>
    <p class="sec-sub">"Pre-Lit" means the lighting is already handled. No hunting for parts, no guessing on electrical — every kit is built and matched to your exact sign.</p>
    <div class="kit-grid">
      <ul class="kit-list">
        <li><span class="chk">&#10003;</span><div><b>Extruded Aluminum Cabinet</b><span>Cut to your exact size from 26' sticks of 4", 7", or 10" extrusion.</span></div></li>
        <li><span class="chk">&#10003;</span><div><b>Welded Corners</b><span>Corners welded in our shop for a rigid, professional frame — not a bolt-together kit frame.</span></div></li>
        <li><span class="chk">&#10003;</span><div><b>Edge-Lit LED Lighting</b><span>LEDs installed inside the cabinet, laid out and matched to your sign's size.</span></div></li>
        <li><span class="chk">&#10003;</span><div><b>12V Power Supply</b><span>The correct power supply for your sign's size and LED load — included, not an add-on.</span></div></li>
        <li><span class="chk">&#10003;</span><div><b>Ships in 4&ndash;6 Pieces</b><span>Sections sized to ship safely nationwide and fit back together on site.</span></div></li>
        <li><span class="chk">&#9432;</span><div><b>Heads Up: Faces &amp; Graphics Not Included</b><span>Kits include everything except the sign panels and graphics. Need faces? Ask about graphics-ready faces or a completed, ready-to-hang cabinet.</span></div></li>
      </ul>
      <img class="ph-img round-img" src="images/diy-kit-assembled-lit.jpg" alt="DIY sign kit assembled and lit by a customer, showing the aluminum cabinet frame with LED lighting glowing">
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <span class="kicker">See It Go Together</span>
    <h2 class="sec-title">Watch a Kit Come Together</h2>
    <p class="sec-sub">From opening the box to flipping the switch — here's what assembling one of our kits actually looks like.</p>
    <div class="video-ph">
      <div class="play">&#9654;</div>
      <b>ASSEMBLY VIDEO</b>
      <span style="max-width:460px;">Your YouTube video embeds here. A simple phone video of a kit going together — even 60&ndash;90 seconds — works great and doubles as content for TikTok and Meta ads.</span>
    </div>
  </div>
</section>
"""

# ---------------- PYLON ----------------
PYLON = """
<section class="page-hero">
  <div class="wrap">
    <span class="kicker">Sign Types Explained</span>
    <h1>Pylon Pole Signs: <span class="lit">Big Visibility</span>, DIY Price</h1>
    <p>The pylon sign is the king of roadside visibility — a lighted cabinet mounted high on a single pole, readable from down the street or off the highway. Here's what they are, how they install, and how our 10" kit gets you one for a fraction of retail.</p>
  </div>
</section>

<section>
  <div class="wrap about-grid">
    <div class="about-copy">
      <span class="kicker">What Is a Pylon Sign?</span>
      <h2 class="sec-title">The Sign Customers See From the Road</h2>
      <p>A pylon (or pole) sign is a freestanding sign mounted on a single steel pole, standing on its own out by the street. Gas stations, shopping centers, restaurants, and businesses set back from the road all rely on them — because a wall sign can't do its job if drivers can't see your wall.</p>
      <p>Our <b>10" wide cabinet</b> is purpose-built for pylon and single-pole mounting. The extra depth gives the cabinet the strength and presence a freestanding sign needs, with the same welded corners and Pre-Lit LED system as every kit we build.</p>
      <p>Like all our kits, it's cut to your size, welded in our shop, and shipped nationwide in sections with the LEDs and power supply included.</p>
    </div>
    <img class="ph-img round-img" src="images/pylon-sign-kit.jpg" alt="DIY single pole pylon sign kit shipped nationwide — heavy duty aluminum frame, LED lighting system, weather resistant, easy to assemble, custom sizes, save up to 60% over local retail">
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <span class="kicker">Install Expectations</span>
    <h2 class="sec-title">What a Pylon Install Involves</h2>
    <p class="sec-sub">A pylon sign is the most involved install we offer — very doable for a contractor or an experienced DIYer, but go in with eyes open.</p>
    <div class="steps">
      <div class="step"><div class="num">1</div><h3>Check Local Requirements</h3><p>Most cities require a sign permit for freestanding signs, and height/size limits vary. Check with your local permitting office before you order — we'll help you spec a cabinet that fits the rules.</p></div>
      <div class="step"><div class="num">2</div><h3>Set the Pole</h3><p>A pylon sign needs a steel pole set in a concrete footing. Pole and concrete are sourced locally (shipping steel pipe nationwide doesn't make sense for anyone).</p></div>
      <div class="step"><div class="num">3</div><h3>Mount the Cabinet</h3><p>Your 10" cabinet arrives in sections, assembles on site, and mounts to the pole. Plan on equipment or extra hands for the lift — this is a two-person-plus job.</p></div>
      <div class="step"><div class="num">4</div><h3>Power It Up</h3><p>Run power to the sign and connect the included 12V supply. Many owners have an electrician handle the final hookup — it's a small job once the sign is up.</p></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <span class="kicker">Other Mounting Styles</span>
    <h2 class="sec-title">Not Going on a Pole?</h2>
    <p class="sec-sub">Every cabinet depth matches a mounting style. If a pylon isn't your setup, one of these is.</p>
    <div class="who-grid">
      <div class="who-card"><div class="ic">&#127970;</div><h3>Wall Mount</h3><p>Flat against the building. Our 4" cabinet (the best seller) — the 7" works here too.</p></div>
      <div class="who-card"><div class="ic">&#128679;</div><h3>Post &amp; Panel</h3><p>Cabinet mounted between ground posts. A clean look for offices and developments — 7" cabinet.</p></div>
      <div class="who-card"><div class="ic">&#9878;&#65039;</div><h3>Double Pole</h3><p>Cabinet carried on two poles for wider signs — 7" cabinet territory.</p></div>
      <div class="who-card"><div class="ic">&#128678;</div><h3>Pylon / Single Pole</h3><p>Maximum roadside visibility on one steel pole — that's the 10" cabinet on this page.</p></div>
    </div>
  </div>
</section>
"""

# ---------------- FAQ ----------------
FAQ = """
<section class="page-hero">
  <div class="wrap">
    <span class="kicker">Questions &amp; Answers</span>
    <h1>Straight Answers From <span class="lit">the Guy Who Builds Them</span></h1>
    <p>Everything customers usually ask before ordering a kit. Don't see your question? Send it through the contact page — you'll get an answer from 20+ years of experience, not a call center.</p>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="faq-list">
      <details open>
        <summary>What does "Pre-Lit" mean?</summary>
        <p>It means the lighting is already built into your kit. Edge-lit LEDs are installed inside the cabinet and matched to your sign's size, and the correct 12V power supply is included in the box. You assemble the cabinet, mount it, and plug it in.</p>
      </details>
      <details>
        <summary>Which cabinet size do I need — 4", 7", or 10"?</summary>
        <p>Rule of thumb: the 4" cabinet is for wall-mounted signs (our best seller), the 7" works on a wall or on double poles and post-and-panel setups, and the 10" is built for pylon and single-pole signs. Not sure? Tell us where the sign is going and we'll steer you right.</p>
      </details>
      <details>
        <summary>How does a big sign ship to me?</summary>
        <p>We build your cabinet, then break it down into 4&ndash;6 pieces sized for safe nationwide shipping. The corners are welded in our shop, and the sections are made to fit back together on site.</p>
      </details>
      <details>
        <summary>Do you install the sign?</summary>
        <p>No — and that's exactly why you save money. We build the sign; you (or your contractor or handyman) install it. Every mounting style has different install expectations, and we'll walk you through what yours involves before you buy.</p>
      </details>
      <details>
        <summary>Do I need to be handy to put one up?</summary>
        <p>If you or someone on your crew can handle basic assembly and mounting, you can put up a wall-mount kit — that's the whole idea. General contractors and handy business owners do it every day. Pole and pylon signs are more involved; see our pylon page for what to expect.</p>
      </details>
      <details>
        <summary>Do I need a permit for my sign?</summary>
        <p>It depends on your city and the type of sign. Wall signs and freestanding signs are often permitted differently, and rules vary a lot from town to town. Check with your local permitting office — and if there are size limits, we'll cut your cabinet to fit them. That's the beauty of made-to-order.</p>
      </details>
      <details>
        <summary>Do you only sell kits, or can I buy a finished sign?</summary>
        <p>Both. Most customers order the DIY kit to maximize savings, but if you'd rather skip the assembly, ask about a completed lighted sign cabinet — built in our shop, graphics-ready, plug and light. Either way, coaching and support are part of the deal: built by you, backed by me.</p>
      </details>
      <details>
        <summary>How much will I really save?</summary>
        <p>Depending on your size and setup, up to about 60% compared to having a local sign company fabricate and install the same sign. You're paying for the sign — not a showroom, a sales office, and an install crew.</p>
      </details>
      <details>
        <summary>Who am I actually buying from?</summary>
        <p>A sign fabricator with 20+ years in the business. Your cabinet is cut, welded, and lit in one shop — and the person quoting your sign is the person building it.</p>
      </details>
      <details>
        <summary>How do I get a price?</summary>
        <p>Every sign is cut to order, so pricing depends on your size and setup. Use the contact page to send your dimensions and mounting style, and we'll come back with the price of your kit, shipped. No obligation, no pushy follow-up.</p>
      </details>
    </div>
  </div>
</section>
"""

# ---------------- CONTACT ----------------
CONTACT = """
<section class="page-hero">
  <div class="wrap">
    <span class="kicker">Contact / Free Quote</span>
    <h1>Tell Us About <span class="lit">Your Sign</span></h1>
    <p>Every sign is cut to order, so pricing depends on your size and setup. Send the details below and we'll get back to you with a straight answer — the price of your kit, shipped.</p>
  </div>
</section>

<section>
  <div class="wrap quote-grid">
    <div class="quote-info">
      <span class="kicker">What to Expect</span>
      <h2 class="sec-title">A Straight Answer, Usually Within a Business Day</h2>
      <p>Fill out what you know — if you're not sure about cabinet size or mounting, leave it blank and describe your situation in the notes. Matching people to the right sign is the part of this job we've done for 20+ years.</p>
      <div class="assure">
        <div><span class="chk">&#10003;</span> No obligation, no pushy follow-up</div>
        <div><span class="chk">&#10003;</span> Quoted personally by the guy who builds it</div>
        <div><span class="chk">&#10003;</span> Kits ship nationwide — we work by email, wherever you are</div>
      </div>
    </div>
""" + QUOTE_FORM + """
  </div>
</section>
"""

# ---------------- LEGAL ----------------
PRIVACY = """
<section class="page-hero">
  <div class="wrap">
    <span class="kicker">Legal</span>
    <h1>Privacy Policy</h1>
    <p>Effective date: July 2026. This policy explains what information diysignguy.com collects and how it's used.</p>
  </div>
</section>
<section>
  <div class="wrap">
    <article class="post">
      <h2>Information We Collect</h2>
      <p>When you submit our quote request form, we collect the information you provide: your name, email address, and any optional details you include (business name, phone number, sign dimensions, mounting preference, and shipping ZIP code). We do not collect payment information through this website.</p>
      <h2>How We Use Your Information</h2>
      <p>We use the information you submit for one purpose: to respond to your quote request and communicate with you about your sign. We do not sell, rent, or share your personal information with third parties for their marketing purposes.</p>
      <h2>Form Processing</h2>
      <p>Quote requests are transmitted to us by a third-party form delivery service, which forwards your submission to our email. That service processes your submission solely to deliver it to us.</p>
      <h2>Cookies &amp; Analytics</h2>
      <p>This site may use analytics tools and advertising pixels (such as Meta or TikTok pixels) to understand site traffic and measure advertising. These tools may set cookies in your browser. You can control cookies through your browser settings, and you can opt out of personalized advertising through the settings of those platforms.</p>
      <h2>Data Retention</h2>
      <p>We keep quote request emails as long as needed to serve you and maintain our business records. You may request deletion of your information at any time by contacting us through the <a href="contact.html">contact page</a>.</p>
      <h2>Children's Privacy</h2>
      <p>This site is intended for business purchasers and is not directed to children under 13. We do not knowingly collect information from children.</p>
      <h2>Changes to This Policy</h2>
      <p>If we update this policy, the new version will be posted on this page with a new effective date.</p>
      <h2>Contact</h2>
      <p>Questions about this policy? Reach us through the <a href="contact.html">contact page</a>.</p>
    </article>
  </div>
</section>
"""

TERMS = """
<section class="page-hero">
  <div class="wrap">
    <span class="kicker">Legal</span>
    <h1>Terms of Use</h1>
    <p>Effective date: July 2026. By using diysignguy.com, you agree to these terms.</p>
  </div>
</section>
<section>
  <div class="wrap">
    <article class="post">
      <h2>About This Site</h2>
      <p>diysignguy.com provides information about our pre-lit aluminum sign cabinet kits and a way to request a quote. Content on this site is provided for general information and is not a binding offer; all sales are quoted individually based on your specifications.</p>
      <h2>Do-It-Yourself Installation — Please Read</h2>
      <p>Our products are kits that <b>you (or your contractor) assemble and install</b>. We do not provide installation services. You are solely responsible for safe assembly, mounting, electrical connection, and compliance with all applicable local building codes, sign ordinances, permit requirements, and electrical codes. Signs are heavy and installation — especially pole and pylon installation — can be dangerous. If you are not confident in any part of the installation, hire a qualified professional. By purchasing a kit, you accept full responsibility for its installation and use.</p>
      <h2>Product Descriptions &amp; Savings Claims</h2>
      <p>We describe our products as accurately as we can. Estimated savings ("up to 60% over local retail") are based on typical retail pricing for comparable fabricated-and-installed signs; your actual savings will vary by market, sign size, and configuration.</p>
      <h2>Quotes &amp; Pricing</h2>
      <p>Because every sign is made to order, prices are provided by individual quote. A quote is valid for the period stated in it and may change if your specifications change.</p>
      <h2>Intellectual Property</h2>
      <p>The content of this site — text, images, and design — belongs to DIY Sign Guy and may not be copied or reused without permission.</p>
      <h2>Disclaimer &amp; Limitation of Liability</h2>
      <p>This website is provided "as is" without warranties of any kind. To the fullest extent permitted by law, DIY Sign Guy is not liable for damages arising from your use of this website or from the assembly, installation, or use of products, beyond the purchase price of the product. Nothing in these terms limits liability that cannot be limited under applicable law.</p>
      <h2>Changes</h2>
      <p>We may update these terms from time to time. The current version will always be posted on this page.</p>
      <h2>Contact</h2>
      <p>Questions? Reach us through the <a href="contact.html">contact page</a>.</p>
    </article>
  </div>
</section>
"""

# ---------------- BLOG POST ----------------
BLOG_POST = """
<section>
  <div class="wrap">
    <article class="post">
      <span class="kicker">Buying Guide</span>
      <h1>Which Sign Cabinet Do I Need — 4", 7", or 10"?</h1>
      <div class="post-meta">From the shop &middot; DIY Sign Guy</div>
      <p>After 20+ years of building signs, the first question I ask every customer is the same one: <b>where is the sign going?</b> Not what size, not what budget — where. Because once you know how a sign will be mounted, the right cabinet picks itself.</p>
      <p>Our kits come in three cabinet depths: 4", 7", and 10". All three are cut from heavy extruded aluminum, welded at the corners, and come Pre-Lit with edge-lit LEDs and the correct 12V power supply. The depth is really about one thing — the mounting style it's built to handle.</p>

      <h2>Going on a wall? That's the 4".</h2>
      <p>The 4" wide cabinet is our best seller for a simple reason: most business signs go flat on the front of a building. The 4" sits low-profile against the wall, lights up evenly, and looks like the sign a local shop would have charged you three times as much to hang. Storefronts, offices, retail strips — this is the workhorse.</p>

      <h2>On posts, or a bigger wall sign? Look at the 7".</h2>
      <p>The 7" wide cabinet is the versatile one. It still works flat on a wall, but the extra depth makes it right for post-and-panel signs and double-pole mounting — the freestanding signs you see in front of offices, medical parks, and developments. If your building sits back from the road and a wall sign won't be seen, this is usually where you land.</p>

      <h2>Up on a pole by the road? That's 10" territory.</h2>
      <p>The 10" wide cabinet is built for pylon and single-pole signs — the big, high-visibility signs on one steel pole that you can read from down the street. It's the most involved install of the three (pole, concrete footing, and usually a permit), but nothing beats it for roadside presence. We cover the details on our <a href="../pylon-signs.html">pylon pole signs page</a>.</p>

      <h2>The cheat sheet</h2>
      <ul>
        <li><b>4" cabinet</b> — wall mount. The best seller.</li>
        <li><b>7" cabinet</b> — wall mount, post &amp; panel, or double pole.</li>
        <li><b>10" cabinet</b> — pylon / single pole.</li>
      </ul>
      <p>Still not sure? That's fine — most people aren't, and guessing wrong is expensive at retail but free with us. <a href="../contact.html">Send us a note</a> with where the sign is going and rough dimensions, and we'll tell you exactly what you need. That answer comes from the guy who'll be cutting and welding your cabinet — not a salesperson.</p>
    </article>
  </div>
</section>
"""

def city_page(city, state, slug):
    content = f"""
<section class="page-hero">
  <div class="wrap">
    <span class="kicker">Now Shipping to {city}, {state}</span>
    <h1>Lighted Business Sign Kits, <span class="lit">Shipped to {city}</span></h1>
    <p>Pre-lit aluminum sign cabinet kits, custom cut to your size, welded in our shop, and delivered anywhere in {city}, {state} — LEDs and power supply included. Skip the local sign-shop markup and save up to 60%.</p>
  </div>
</section>

<section>
  <div class="wrap about-grid">
    <div class="about-copy">
      <span class="kicker">A Better Way to Buy a Sign in {city}</span>
      <h2 class="sec-title">The Same Sign. Without the Retail Markup.</h2>
      <p>If you've priced a lighted sign from a sign company in {city}, you already know: the quote isn't really for the sign. It's for the showroom, the sales team, and the install crew that come with it.</p>
      <p>We do it differently. Your cabinet is <b>cut to your exact size</b> from 26-foot sticks of extruded aluminum, <b>corners welded by hand</b>, fitted with edge-lit LEDs and the correct 12V power supply — then shipped straight to your door in {city} in 4&ndash;6 pieces sized for safe freight.</p>
      <p>You or your contractor handle the install, and you keep the difference — typically <b>up to 60% off local retail</b>. It's how contractors, developers, and business owners across {state} have been putting up professional signs without professional-sign prices.</p>
      <a href="../contact.html" class="btn btn-amber" style="margin-top:8px;">Get a Quote for Your {city} Sign</a>
    </div>
    <img class="ph-img round-img" src="../images/storefront-cabinet-blank.jpg" alt="LED-lighted sign cabinet glowing on a brick storefront at night, ready for business graphics">
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <span class="kicker">Our Kits</span>
    <h2 class="sec-title">Three Cabinets for Every {city} Sign</h2>
    <div class="who-grid" style="grid-template-columns:repeat(3,1fr);">
      <div class="who-card"><div class="ic">&#127970;</div><h3>4" Cabinet — Wall Mount</h3><p>Our best seller. Low-profile lighted storefront signs for shops, offices, and retail strips.</p></div>
      <div class="who-card"><div class="ic">&#128679;</div><h3>7" Cabinet — Wall / Double-Pole</h3><p>The versatile middle weight — wall mount, post &amp; panel, or double-pole freestanding signs.</p></div>
      <div class="who-card"><div class="ic">&#128678;</div><h3>10" Cabinet — Pylon / Single Pole</h3><p>Heavy-duty roadside visibility on a single pole. Built for pylon signs.</p></div>
    </div>
    <p style="margin-top:30px;color:var(--muted);">Every kit ships to {city} with welded corners, edge-lit LEDs, and the correct power supply included. <a href="../kits.html" style="color:var(--amber-text);font-weight:700;">See full kit details &rarr;</a></p>
  </div>
</section>

<section>
  <div class="wrap">
    <span class="kicker">Who Orders From Us in {state}</span>
    <h2 class="sec-title">Built for People Who'd Rather Not Pay Sign-Shop Prices</h2>
    <div class="who-grid">
      <div class="who-card"><div class="ic">&#127978;</div><h3>Small Business Owners</h3><p>The lighted sign your {city} storefront deserves, without the retail markup.</p></div>
      <div class="who-card"><div class="ic">&#127959;&#65039;</div><h3>General Contractors</h3><p>Add signage to your scope. We build the cabinet, your crew installs, you keep the margin.</p></div>
      <div class="who-card"><div class="ic">&#127960;&#65039;</div><h3>Developers</h3><p>Post-and-panel and pylon cabinets for projects across the {city} area.</p></div>
      <div class="who-card"><div class="ic">&#127968;</div><h3>Real Estate Offices</h3><p>Professional lighted presence at a price that makes sense.</p></div>
    </div>
  </div>
</section>
"""
    page(f"cities/{slug}.html",
         f"Business Sign Kits Shipped to {city}, {state} | DIY Sign Guy",
         f"Pre-lit aluminum sign cabinet kits custom cut to size and shipped to {city}, {state}. Welded corners, LEDs and power supply included. Save up to 60% vs {city} sign shops.",
         None, content, root="../")

# Cities: add (City, ST, url-slug) tuples here and rerun.
CITIES = [
    ("Dallas", "TX", "dallas-tx"),
    ("Oklahoma City", "OK", "oklahoma-city-ok"),
]

if __name__ == "__main__":
    page("index.html", "DIY Sign Guy — Pre-Lit Aluminum Sign Cabinet Kits, Shipped Nationwide",
         "Pre-lit aluminum sign cabinet kits custom cut to your size, welded corners, LEDs and power supply included. Ships nationwide. Save up to 60% over local retail. 20+ years in the sign business.",
         "home", HOME)
    page("kits.html", "Our Shop Kits — 4\", 7\" & 10\" Pre-Lit Sign Cabinets | DIY Sign Guy",
         "Compare our 4\", 7\" and 10\" pre-lit aluminum sign cabinet kits. Every kit includes welded corners, edge-lit LEDs, and a 12V power supply — cut to your size, shipped nationwide.",
         "kits", KITS)
    page("pylon-signs.html", "Pylon Pole Signs Explained — DIY Pylon Sign Kits | DIY Sign Guy",
         "What a pylon pole sign is, what the install involves, and how our 10\" pre-lit cabinet kit gets you roadside visibility for up to 60% less than retail.",
         "pylon", PYLON)
    page("faq.html", "Questions & Answers — DIY Sign Kits | DIY Sign Guy",
         "Straight answers about our pre-lit sign cabinet kits: what's included, how signs ship, which cabinet you need, permits, installation, and savings.",
         "faq", FAQ)
    page("contact.html", "Contact / Get a Free Quote | DIY Sign Guy",
         "Get a free quote on a pre-lit aluminum sign cabinet kit, cut to your size and shipped nationwide. No obligation — quoted by the guy who builds it.",
         "contact", CONTACT)
    page("privacy.html", "Privacy Policy | DIY Sign Guy",
         "How diysignguy.com collects and uses information submitted through our quote request form.",
         None, PRIVACY)
    page("terms.html", "Terms of Use | DIY Sign Guy",
         "Terms of use for diysignguy.com, including important information about do-it-yourself sign installation responsibility.",
         None, TERMS)
    page("blog/which-sign-cabinet-do-i-need.html",
         "Which Sign Cabinet Do I Need — 4\", 7\", or 10\"? | DIY Sign Guy",
         "The simple rule of thumb for choosing between a 4\", 7\", and 10\" sign cabinet, from a fabricator with 20+ years in the sign business.",
         None, BLOG_POST, root="../")
    for c, s, slug in CITIES:
        city_page(c, s, slug)
    print("done")
