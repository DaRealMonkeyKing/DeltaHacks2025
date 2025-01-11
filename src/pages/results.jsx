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
              src="src\assets\react.svg" 
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
            className="px-6 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 transition-colors"
          >
            Try Again
          </Link>
          <Link 
            to="/upload" 
            className="px-6 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 transition-colors"
          >
            New Topic
          </Link>
        </div>
      </div>
    </div>
  )
}
