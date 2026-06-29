import { useState, useRef, useEffect } from 'react'

const API = 'http://localhost:8000'

const SendIcon = () => (
  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
    <path d="M22 2L11 13M22 2l-7 20-4-9-9-4 20-7z"/>
  </svg>
)

const CloseIcon = () => (
  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5">
    <path d="M18 6L6 18M6 6l12 12"/>
  </svg>
)

const Spinner = () => (
  <span style={{ display: 'inline-flex', gap: 4, alignItems: 'center', padding: '2px 0' }}>
    {[0, 1, 2].map(i => (
      <span key={i} style={{
        width: 6, height: 6, borderRadius: '50%', background: '#818cf8',
        animation: 'bounce 1.1s infinite ease-in-out', animationDelay: `${i * 0.18}s`
      }} />
    ))}
    <style>{`@keyframes bounce{0%,80%,100%{transform:translateY(0)}40%{transform:translateY(-5px)}}`}</style>
  </span>
)

export default function App() {
  const [open, setOpen] = useState(false)
  const [messages, setMessages] = useState([
    { role: 'assistant', text: 'Hi! Ask me anything about energy data, customers, or orders.' }
  ])
  const [input, setInput] = useState('')
  const [loading, setLoading] = useState(false)
  const bottomRef = useRef(null)
  const inputRef = useRef(null)

  useEffect(() => {
    if (open) {
      bottomRef.current?.scrollIntoView({ behavior: 'smooth' })
      setTimeout(() => inputRef.current?.focus(), 80)
    }
  }, [open, messages, loading])

  const send = async () => {
    const query = input.trim()
    if (!query || loading) return
    setInput('')
    setMessages(prev => [...prev, { role: 'user', text: query }])
    setLoading(true)
    try {
      const res = await fetch(`${API}/chatbot/agent?query=${encodeURIComponent(query)}`, { method: 'POST'})
      const data = await res.json()
      setMessages(prev => [...prev, { role: 'assistant', text: data.response ?? 'No response.' }])
    } catch {
      setMessages(prev => [...prev, { role: 'assistant', text: '⚠️ Could not reach backend.', error: true }])
    } finally {
      setLoading(false)
    }
  }

  const onKey = e => e.key === 'Enter' && !e.shiftKey && (e.preventDefault(), send())

  return (
    <>
      <style>{`
        .chat-widget { position: fixed; bottom: 28px; right: 28px; z-index: 9999; font-family: 'Inter', sans-serif; }
        .fab { width: 56px; height: 56px; border-radius: 50%; background: linear-gradient(135deg,#4f46e5,#7c3aed);
          border: none; cursor: pointer; display: flex; align-items: center; justify-content: center;
          box-shadow: 0 4px 24px rgba(79,70,229,.5); transition: transform .2s, box-shadow .2s; }
        .fab:hover { transform: scale(1.08); box-shadow: 0 6px 32px rgba(79,70,229,.65); }
        .fab svg { transition: transform .25s; }
        .panel { position: absolute; bottom: 70px; right: 0; width: 340px; height: 480px;
          background: #13151d; border: 1px solid #1e2433; border-radius: 20px;
          display: flex; flex-direction: column; overflow: hidden;
          box-shadow: 0 16px 56px rgba(0,0,0,.6);
          transform-origin: bottom right;
          animation: popIn .22s cubic-bezier(.34,1.56,.64,1); }
        @keyframes popIn { from { opacity:0; transform:scale(.85) translateY(12px); } to { opacity:1; transform:scale(1) translateY(0); } }
        .panel-header { padding: 14px 16px; background: #0f1117; border-bottom: 1px solid #1e2433;
          display: flex; align-items: center; gap: 10; justify-content: space-between; }
        .header-left { display: flex; align-items: center; gap: 10px; }
        .header-avatar { width: 32px; height: 32px; border-radius: 50%; background: linear-gradient(135deg,#4f46e5,#7c3aed);
          display: flex; align-items: center; justify-content: center; }
        .header-info { display: flex; flex-direction: column; }
        .header-name { font-size: 14px; font-weight: 600; color: #f1f5f9; }
        .header-status { font-size: 11px; color: #64748b; display: flex; align-items: center; gap: 5px; }
        .status-dot { width: 6px; height: 6px; border-radius: 50%; background: #22c55e; display: inline-block; }
        .close-btn { background: none; border: none; cursor: pointer; color: #475569; padding: 4px;
          border-radius: 6px; display: flex; transition: color .15s; }
        .close-btn:hover { color: #e2e8f0; }
        .messages { flex: 1; overflow-y: auto; padding: 14px 14px; display: flex; flex-direction: column; gap: 10; }
        .messages::-webkit-scrollbar { width: 4px; }
        .messages::-webkit-scrollbar-thumb { background: #1e2433; border-radius: 4px; }
        .row { display: flex; align-items: flex-end; gap: 7px; }
        .bubble { max-width: 82%; padding: 9px 13px; border-radius: 14px; font-size: 13px;
          line-height: 1.6; white-space: pre-wrap; word-break: break-word; }
        .bubble-bot { background: #181d2b; border: 1px solid #1e2b45; border-bottom-left-radius: 3px; color: #cbd5e1; }
        .bubble-user { background: #4f46e5; border-bottom-right-radius: 3px; color: #fff; margin-left: auto; }
        .bubble-error { background: #1e1215 !important; border-color: #7f1d1d !important; }
        .mini-avatar { width: 24px; height: 24px; border-radius: 50%; background: #1e1b4b; color: #818cf8;
          display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
        .input-area { padding: 10px 12px; border-top: 1px solid #1e2433; display: flex; gap: 8px; align-items: flex-end; }
        textarea.chat-input { flex: 1; background: #0f1117; border: 1px solid #1e2b45; border-radius: 10px;
          padding: 9px 12px; color: #e2e8f0; font-size: 13px; resize: none; outline: none;
          font-family: inherit; line-height: 1.5; max-height: 100px; overflow-y: auto; }
        textarea.chat-input::placeholder { color: #334155; }
        .send-btn { width: 36px; height: 36px; border-radius: 9px; border: none;
          background: #4f46e5; color: #fff; cursor: pointer; display: flex;
          align-items: center; justify-content: center; flex-shrink: 0; transition: opacity .2s; }
      `}</style>

      <div className="chat-widget">
        {open && (
          <div className="panel">
            <div className="panel-header">
              <div className="header-left">
                <div className="header-avatar">
                  <BotSvg size={16} />
                </div>
                <div className="header-info">
                  <span className="header-name">Energy transfo Agent </span>
                  <span className="header-status"><span className="status-dot" />Online</span>
                </div>
              </div>
              <button className="close-btn" onClick={() => setOpen(false)}><CloseIcon /></button>
            </div>

            <div className="messages">
              {messages.map((m, i) => (
                <div key={i} className="row" style={{ justifyContent: m.role === 'user' ? 'flex-end' : 'flex-start' }}>
                  {m.role === 'assistant' && <div className="mini-avatar"><BotSvg size={12} /></div>}
                  <div className={`bubble ${m.role === 'user' ? 'bubble-user' : 'bubble-bot'}${m.error ? ' bubble-error' : ''}`}>
                    {m.text}
                  </div>
                </div>
              ))}
              {loading && (
                <div className="row">
                  <div className="mini-avatar"><BotSvg size={12} /></div>
                  <div className="bubble bubble-bot"><Spinner /></div>
                </div>
              )}
              <div ref={bottomRef} />
            </div>

            <div className="input-area">
              <textarea
                ref={inputRef}
                className="chat-input"
                rows={1}
                placeholder="Ask something…"
                value={input}
                onChange={e => setInput(e.target.value)}
                onKeyDown={onKey}
              />
              <button className="send-btn" style={{ opacity: (!input.trim() || loading) ? 0.35 : 1 }} onClick={send}>
                <SendIcon />
              </button>
            </div>
          </div>
        )}

        <button className="fab" onClick={() => setOpen(o => !o)} aria-label="Toggle chat">
          {open ? <CloseIcon /> : <BotSvg size={24} color="#fff" />}
        </button>
      </div>
    </>
  )
}

const BotSvg = ({ size = 20, color = '#818cf8' }) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke={color} strokeWidth="2">
    <rect x="3" y="11" width="18" height="10" rx="2"/>
    <circle cx="12" cy="5" r="2"/>
    <path d="M12 7v4M8 15h.01M16 15h.01"/>
  </svg>
)
