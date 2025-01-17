import React from 'react'
import { Link } from 'react-router-dom'


 // TODO: make it less ugly
export default function Hero() {
  return <div className="flex-1 flex flex-col md:flex-row items-center max-w-7xl mx-auto px-8 gap-8 md:gap-16 py-8 bg-primary text-white">
    <div className="min-h-screen flex flex-col min-w-full">
      <header className="flex fixed top-0 left-0 right-0 justify-between items-center px-8 py-4 bg-background shadow-md z-50">
        <div className="h-10">
          <Link to="/">
            <img 
              src="src\assets\logo.png" 
              alt="Logo" 
              className="h-full w-auto "
            />
          </Link>
        </div>
        <Link 
          to="/login" 
          className="px-6 py-2 bg-primary text-background rounded-md hover:bg-accent transition-colors"
        >
          Login
        </Link>
      </header>

      <main className="flex-1 flex items-center max-w-7xl mx-auto px-8 gap-16 min-h-screen">
        <div className="flex-1">
          <img 
            src="src\assets\stego.png" 
            alt="Featured" 
            className="max-w-lg aspect-square object-contain bg-white rounded-full p-1 hover:animate-spin-slow"
          />
        </div>
        <div className="flex-1 space-y-4">
          <h1 className="text-6xl font-bold text-white">
            StegoStudy
          </h1>
          <p className="text-2xl text-blue-50 leading-relaxed">
            Achieve all your learning goals with a fun and interactive study pal! (Scientifically proven!!!!)
          </p>
        </div>
      </main>
    </div>
  </div>
}
