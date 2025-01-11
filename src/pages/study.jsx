import React from 'react'
import { Link } from 'react-router-dom'

export default function study() {
  return (
    <div>
      <header className="flex fixed top-0 left-0 right-0 justify-between items-center px-8 py-4 bg-white shadow-md">
        <div className="h-10">
          <Link to="/">
            <img 
              src="src\assets\logo.png" 
              alt="Logo" 
              className="h-full w-auto"
            />
          </Link>
        </div>
      </header>
      <div className="flex items-center justify-center min-h-screen">
        <div className="text-center">
          <p>study page with ai</p>
          <button className="px-6 py-2 bg-red-400 text-background rounded-md hover:bg-red-500 transition-colors">Record</button>
          <Link 
            to="/results" 
          
          >
            <button className="px-6 py-2 bg-primary text-background rounded-md hover:bg-accent transition-colors">Results</button>
          </Link>
        </div>
      </div>
    </div>
  )
}

