with open(r'c:/Users/farze/Downloads/funoonai website/funoon-ai-website.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ── CSS ──
css = """
/* ===== CHATBOT ===== */
#chat-widget {
  position: fixed;
  bottom: 28px; right: 28px;
  z-index: 9990;
  font-family: var(--font-body);
  display: flex;
  flex-direction: column;
  align-items: flex-end;
}
#chat-toggle {
  width: 56px; height: 56px;
  border-radius: 50%;
  background: var(--gold);
  border: none;
  cursor: none;
  display: flex; align-items: center; justify-content: center;
  box-shadow: 0 6px 24px rgba(255,243,234,0.2);
  transition: transform 0.25s ease, box-shadow 0.25s ease;
  flex-shrink: 0;
}
#chat-toggle:hover { transform: scale(1.08); box-shadow: 0 10px 32px rgba(255,243,234,0.3); }
#chat-toggle .icon-chat { display: block; }
#chat-toggle .icon-close { display: none; }
#chat-toggle.open .icon-chat { display: none; }
#chat-toggle.open .icon-close { display: block; }
#chat-panel {
  width: 320px;
  background: var(--bg2);
  border: 1px solid var(--border2);
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 20px 60px rgba(0,0,0,0.6);
  margin-bottom: 12px;
  display: none;
  flex-direction: column;
  max-height: 480px;
}
#chat-panel.open {
  display: flex;
  animation: cbOpen 0.28s cubic-bezier(0.34,1.56,0.64,1) forwards;
}
@keyframes cbOpen {
  from { opacity:0; transform:translateY(16px) scale(0.96); }
  to   { opacity:1; transform:translateY(0) scale(1); }
}
.cb-header {
  background: var(--surface);
  padding: 14px 16px;
  display: flex; align-items: center; gap: 10px;
  border-bottom: 1px solid var(--border);
  flex-shrink: 0;
}
.cb-avatar {
  width: 36px; height: 36px; border-radius: 50%;
  background: var(--surface2);
  display: flex; align-items: center; justify-content: center;
  flex-shrink: 0;
  overflow: hidden;
}
.cb-avatar img { width: 22px; height: 22px; object-fit: contain; }
.cb-name { font-size: 13px; font-weight: 700; color: var(--white); }
.cb-status { font-size: 11px; color: var(--wa); display: flex; align-items: center; gap: 4px; margin-top: 1px; }
.cb-dot { width: 5px; height: 5px; border-radius: 50%; background: var(--wa); animation: pulse-dot 1.8s infinite; }
.cb-body {
  flex: 1; overflow-y: auto;
  padding: 14px;
  display: flex; flex-direction: column; gap: 8px;
  scrollbar-width: thin; scrollbar-color: var(--border2) transparent;
}
.cb-body::-webkit-scrollbar { width: 3px; }
.cb-body::-webkit-scrollbar-thumb { background: var(--border2); border-radius: 2px; }
.cb-msg {
  max-width: 82%; padding: 9px 13px; border-radius: 13px;
  font-size: 13px; line-height: 1.5;
  opacity: 0; transform: translateY(5px);
  transition: opacity 0.25s ease, transform 0.25s ease;
  white-space: pre-line;
}
.cb-msg.show { opacity: 1; transform: translateY(0); }
.cb-msg.bot {
  background: var(--surface2); border: 1px solid var(--border);
  align-self: flex-start; border-bottom-left-radius: 3px; color: var(--white);
}
.cb-msg.user {
  background: var(--gold); color: #000;
  align-self: flex-end; border-bottom-right-radius: 3px; font-weight: 500;
}
.cb-typing {
  display: flex; gap: 4px; align-items: center;
  padding: 9px 13px;
  background: var(--surface2); border: 1px solid var(--border);
  border-radius: 13px 13px 13px 3px;
  align-self: flex-start; width: 50px;
}
.cb-typing span {
  width: 5px; height: 5px; background: var(--white-faint);
  border-radius: 50%; animation: typingBounce 1.2s ease infinite;
}
.cb-typing span:nth-child(2) { animation-delay: 0.16s; }
.cb-typing span:nth-child(3) { animation-delay: 0.32s; }
.cb-footer {
  padding: 10px 12px; border-top: 1px solid var(--border);
  display: flex; gap: 8px; flex-shrink: 0; background: var(--surface);
}
#cb-input {
  flex: 1; background: var(--bg2); border: 1px solid var(--border2);
  border-radius: 9px; padding: 9px 12px; font-size: 13px;
  color: var(--white); font-family: var(--font-body); outline: none;
  transition: border-color 0.2s;
}
#cb-input::placeholder { color: var(--white-faint); }
#cb-input:focus { border-color: var(--gold); }
#cb-send {
  width: 36px; height: 36px; background: var(--gold); border: none;
  border-radius: 9px; cursor: none;
  display: flex; align-items: center; justify-content: center;
  flex-shrink: 0; transition: transform 0.2s;
}
#cb-send:hover { transform: scale(1.08); }
#cb-send svg { width: 14px; height: 14px; }
.cb-quick {
  display: flex; flex-wrap: wrap; gap: 5px; margin-top: 2px;
}
.cb-qr {
  padding: 5px 11px; background: transparent;
  border: 1px solid var(--border2); border-radius: 100px;
  font-size: 11px; color: var(--white-dim); cursor: none;
  transition: all 0.2s; font-family: var(--font-body);
}
.cb-qr:hover { border-color: var(--gold); color: var(--gold); }
"""

# ── HTML ──
html = """<!-- CHATBOT -->
<div id="chat-widget">
  <div id="chat-panel">
    <div class="cb-header">
      <div class="cb-avatar">
        <img src="src/funoon%20ai%20without%20bg%20svg/2.svg" alt="Wasel">
      </div>
      <div>
        <div class="cb-name">Wasel &mdash; &#x648;&#x627;&#x635;&#x644;</div>
        <div class="cb-status"><span class="cb-dot"></span>Online now</div>
      </div>
    </div>
    <div class="cb-body" id="cb-body"></div>
    <div class="cb-footer">
      <input type="text" id="cb-input" placeholder="Ask anything..." autocomplete="off">
      <button id="cb-send">
        <svg viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
          <line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/>
        </svg>
      </button>
    </div>
  </div>
  <button id="chat-toggle">
    <svg class="icon-chat" viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
    </svg>
    <svg class="icon-close" viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="2.5" stroke-linecap="round">
      <line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/>
    </svg>
  </button>
</div>
"""

# ── JS ── (all strings on single lines, no literal newlines)
js = r"""
// ===== CHATBOT =====
document.addEventListener('DOMContentLoaded', function () {
  var tog   = document.getElementById('chat-toggle');
  var panel = document.getElementById('chat-panel');
  var bd    = document.getElementById('cb-body');
  var inp   = document.getElementById('cb-input');
  var snd   = document.getElementById('cb-send');
  var started = false;

  var intro = [
    { role:'bot', text:"Ahlan! I'm Wasel, funoon.ai's AI assistant. How can I help?", delay:600 },
    { role:'bot', isQR:true, opts:['See a Demo','Pricing','How it works','Talk to a human'], delay:1200 }
  ];

  var flows = {
    'see a demo':[
      { role:'bot', text:'Our demo shows Wasel qualifying a real lead live in front of you.', delay:800 },
      { role:'bot', text:'Book a slot at hello@funoon.ai — we confirm within 2 hours.', delay:1600 }
    ],
    'pricing':[
      { role:'bot', text:'3 plans from AED 499/month. Growth (AED 999) is most popular for dealerships.', delay:800 },
      { role:'bot', text:'All plans include a free pilot. Want the full breakdown?', delay:1700 }
    ],
    'how it works':[
      { role:'bot', text:'1. Lead messages your WhatsApp\n2. Wasel qualifies in Arabic, English, or Hinglish\n3. Hot leads escalated to your sales team instantly.', delay:800 }
    ],
    'talk to a human':[
      { role:'bot', text:'Sure! Reach our team at hello@funoon.ai or WhatsApp wa.me/971000000000', delay:700 },
      { role:'bot', text:'We reply within 2 hours.', delay:1400 }
    ]
  };

  var fallback = [
    { role:'bot', text:'Good question! Our team can answer that properly.', delay:700 },
    { role:'bot', text:'Drop us a line at hello@funoon.ai — we reply within 2 hours.', delay:1400 }
  ];

  tog.addEventListener('click', function () {
    var open = panel.classList.toggle('open');
    tog.classList.toggle('open', open);
    if (open && !started) { started = true; runFlow(intro, 0); }
  });

  function runFlow(flow, i) {
    if (i >= flow.length) return;
    var msg = flow[i];
    setTimeout(function () {
      if (msg.isQR) { addQR(msg.opts); runFlow(flow, i + 1); return; }
      showTyping(function () { addMsg(msg.role, msg.text); runFlow(flow, i + 1); }, 650);
    }, msg.delay);
  }

  function addMsg(role, text) {
    var el = document.createElement('div');
    el.className = 'cb-msg ' + role;
    el.textContent = text;
    bd.appendChild(el);
    bd.scrollTop = bd.scrollHeight;
    setTimeout(function () { el.classList.add('show'); }, 20);
  }

  function addQR(opts) {
    var wrap = document.createElement('div');
    wrap.className = 'cb-quick';
    opts.forEach(function (opt) {
      var b = document.createElement('button');
      b.className = 'cb-qr';
      b.textContent = opt;
      b.onclick = function () { onSend(opt); };
      wrap.appendChild(b);
    });
    bd.appendChild(wrap);
    bd.scrollTop = bd.scrollHeight;
  }

  function showTyping(cb, delay) {
    var t = document.createElement('div');
    t.className = 'cb-typing';
    t.innerHTML = '<span></span><span></span><span></span>';
    bd.appendChild(t);
    bd.scrollTop = bd.scrollHeight;
    setTimeout(function () { t.remove(); cb(); }, delay);
  }

  function onSend(text) {
    if (!text) return;
    document.querySelectorAll('.cb-quick').forEach(function (el) { el.remove(); });
    addMsg('user', text);
    var key = text.toLowerCase().replace(/[^a-z ]/g, '').trim();
    runFlow(flows[key] || fallback, 0);
  }

  snd.addEventListener('click', function () {
    var v = inp.value.trim();
    if (!v) return;
    inp.value = '';
    onSend(v);
  });

  inp.addEventListener('keydown', function (e) {
    if (e.key === 'Enter') { snd.click(); }
  });
});
"""

content = content.replace('</style>', css + '\n</style>', 1)
content = content.replace('</body>', html + '\n</body>', 1)
# Inject into the LAST </script> so DOM elements exist
parts = content.rsplit('</script>', 1)
content = parts[0] + js + '\n</script>' + parts[1]

with open(r'c:/Users/farze/Downloads/funoonai website/funoon-ai-website.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done, size:', len(content))
