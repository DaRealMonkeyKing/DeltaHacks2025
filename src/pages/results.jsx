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
          <h1 className="text-6xl font-bold text-primary pt-20">Let's see how you did!</h1>
          <div className="flex items-center justify-center">
            <img src="src\assets\pizza.png" alt="Mascot" className="w-2/3" />
          </div>
          <h2 className="text-3xl text-gray-800 font-semibold p-2">StegoStudy heard 83% of key information in the study set.</h2>
          <h2 className="text-3xl text-gray-800 font-semibold p-2">Here's what you missed:</h2>
          <p> add stuff here</p>
          <h2 className="text-3xl text-gray-800 font-semibold p-4">Study again?</h2>
          <div className="flex justify-center items-center gap-4 pt-2 pb-10">
            <Link 
              to="/study">
              <button className="w-[300px] py-4 bg-primary text-2xl text-background rounded-md hover:accent transition-colors">Try Again</button>
            </Link>
            <Link 
              to="/upload">
              <button className="w-[300px] py-4 bg-primary text-2xl text-background rounded-md hover:accent transition-colors">New Topic</button>
            </Link>
          </div>
        </div>
      </div>
    </div>
  )
}
