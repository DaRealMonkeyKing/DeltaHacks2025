import React from 'react'
import { Link } from 'react-router-dom'

export default function upload() {
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
          <p>Upload/choose a study set page</p>
          <Link 
            to="/study" 
          >
            <button className="bg-primary text-background rounded-md px-10 py-2">Study</button>
          </Link>
        </div>
      </div>
    </div>
  )
}
