import { BrowserRouter, Routes, Route, Link } from 'react-router-dom'
import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import Home from './pages/home'
import Login from './pages/login'
import Upload from './pages/upload'
import Study from './pages/study'
import Results from './pages/results'
import './App.css'

function App() {
  return (
    <div className="max-w-screen">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/upload" element={<Upload />} />
          <Route path="/study" element={<Study />} />
          <Route path="/results" element={<Results />} />
        </Routes>
      </BrowserRouter>
    </div>
  )
}

export default App
