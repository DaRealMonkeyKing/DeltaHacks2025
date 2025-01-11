import React from 'react'
import { Link } from 'react-router-dom'

export default function results() {
  return (
    <div>
      <header className="flex fixed top-0 left-0 right-0 justify-between items-center px-8 py-4 bg-white shadow-md">
        <div className="h-10">
          {/* Replace with your logo */}
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

          <p>results page</p>
          <p>button to choose a new file and button to study same thing again</p>
          <Link 
            to="/study" 
            
          >
            <button className="px-6 py-2 bg-primary text-background rounded-md hover:bg-accent transition-colors">Try Again</button>
          </Link>
          <Link 
            to="/upload" 
            
          >
            <button className="px-6 py-2 bg-primary text-background rounded-md hover:bg-accent transition-colors">New Topic</button>
          </Link>
        </div>
      </div>
    </div>
  )
}
