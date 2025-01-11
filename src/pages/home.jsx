import React from 'react'
import { Link } from 'react-router-dom'
import VoiceRecorder from '../VoiceRecorder'

export default function Home() {
  return <div className="flex-1 flex flex-col md:flex-row items-center max-w-7xl mx-auto px-8 gap-8 md:gap-16 py-8">
    <div className="min-h-screen flex flex-col min-w-full">
      <header className="flex fixed top-0 left-0 right-0 justify-between items-center px-8 py-4 bg-white shadow-md">
        <div className="h-10">
          {/* Replace with your logo */}
          <img 
            src="src\assets\react.svg" 
            alt="Logo" 
            className="h-full w-auto"
          />
        </div>
        <Link 
          to="/login" 
          className="px-6 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 transition-colors"
        >
          Login
        </Link>
      </header>

      <main className="flex-1 flex items-center max-w-7xl mx-auto px-8 gap-16">
        <div className="flex-1">
          {/* Replace with your image */}
          <img 
            src="src\assets\react.svg" 
            alt="Featured" 
            className="w-full h-auto rounded-lg shadow-lg"
          />
        </div>
        <div className="flex-1 space-y-4">
          <h1 className="text-4xl font-bold text-gray-800">
            Study website
          </h1>
          <p className="text-lg text-gray-600 leading-relaxed">
            some paragraph text
          </p>
        </div>
      </main>
    </div>
  </div>
}
