import React from 'react'
import { Link } from 'react-router-dom'
import VoiceRecorder from '../VoiceRecorder'


 // TODO: change font to poppins
 // TODO: make it less ugly
export default function Home() {
  return <div className="flex-1 flex flex-col md:flex-row items-center max-w-7xl mx-auto px-8 gap-8 md:gap-16 py-8">
    <div className="min-h-screen flex flex-col min-w-full">
      <header className="flex fixed top-0 left-0 right-0 justify-between items-center px-8 py-4 bg-background shadow-md">
        <div className="h-10">
          <img 
            src="src\assets\mascot.png" 
            alt="Logo" 
            className="h-full w-auto scale-x-[-1]"
          />
        </div>
        <Link 
          to="/login" 
          className="px-6 py-2 bg-primary text-background rounded-md hover:bg-accent transition-colors"
        >
          Login
        </Link>
      </header>

      <main className="flex-1 flex items-center max-w-7xl mx-auto px-8 gap-16 bg-gradient-to-b from-white to-accent min-h-screen">
        <div className="flex-1">
          <img 
            src="src\assets\mascot.png" 
            alt="Featured" 
            className="w-full h-auto scale-x-[-1]"
          />
        </div>
        <div className="flex-1 space-y-4">
          <h1 className="text-4xl font-bold text-primary">
            Placeholder Name
          </h1>
          <p className="text-lg text-secondary leading-relaxed">
            Placeholder description
          </p>
        </div>
      </main>
    </div>
  </div>
}
