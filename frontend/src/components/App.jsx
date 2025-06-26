import React, { useState } from 'react'
import axios from 'axios'

export default function App() {
  const [file, setFile] = useState(null)
  const [loading, setLoading] = useState(false)
  const [resumo, setResumo] = useState("")
  const [relatorios, setRelatorios] = useState(null)

  const handleUpload = async () => {
    if (!file) return alert("Selecione um vídeo.")

    const formData = new FormData()
    formData.append("file", file)

    setLoading(true)
    try {
      const response = await axios.post("https://SEU-BACKEND.up.railway.app/upload/", formData)
      setResumo(response.data.resumo)
      setRelatorios(response.data.relatorios)
    } catch (err) {
      alert("Erro ao enviar vídeo: " + err.message)
    }
    setLoading(false)
  }

  return (
    <div>
      <h2>Teste de Acessibilidade com IA</h2>
      <input type="file" accept="video/mp4,video/webm" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={handleUpload} disabled={loading} style={{ marginLeft: 10 }}>
        {loading ? "Analisando..." : "Enviar"}
      </button>

      {resumo && (
        <div style={{ marginTop: 30 }}>
          <h3>Resumo da Análise</h3>
          <pre>{resumo}</pre>

          {relatorios && (
            <div>
              <h4>Relatórios:</h4>
              <a href={`https://SEU-BACKEND.up.railway.app/${relatorios.pdf}`} target="_blank" rel="noreferrer">📄 Baixar PDF</a><br />
              <a href={`https://SEU-BACKEND.up.railway.app/${relatorios.markdown}`} target="_blank" rel="noreferrer">📝 Baixar Markdown</a>
            </div>
          )}
        </div>
      )}
    </div>
  )
}
