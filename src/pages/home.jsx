import React from 'react'
import { Link } from 'react-router-dom'


 // TODO: make it less ugly
export default function Home() {
  return <div className="flex-1 flex flex-col md:flex-row items-center max-w-7xl mx-auto px-8 gap-8 md:gap-16 py-8">
    <div className="min-h-screen flex flex-col min-w-full">
      <header className="flex fixed top-0 left-0 right-0 justify-between items-center px-8 py-4 bg-background shadow-md z-50">
        <div className="h-10">
          <Link to="/">
            <img 
              src="src\assets\logo.png" 
              alt="Logo" 
              className="h-full w-auto"
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
            src="src\assets\mascot.png" 
            alt="Featured" 
            className="w-full h-auto scale-x-[-1]"
          />
        </div>
        <div className="flex-1 space-y-4">
          <h1 className="text-6xl font-bold text-primary">
            StegoStudy
          </h1>
          <p className="text-2xl text-secondary leading-relaxed">
            Achieve all your learning goals with a fun and interactive study pal! (Scientifically proven!!!!)
          </p>
        </div>
      </main>
    </div>
  </div>
}
