import React from 'react'
import { Link } from 'react-router-dom'

export default function CustomizeUpload() {
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
        <h2 className="text-3xl text-gray-800 font-semibold p-4">Customize your study set!</h2>
        <p>maybe we can finish this later</p>
      </div>
    </div>
  )
}
