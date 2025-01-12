import React from 'react'
import { Link } from 'react-router-dom'
import VoiceRecorder from '../VoiceRecorder'
import VoiceRecorder from '../VoiceRecorder'

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
          <h1 className="text-6xl text-primary font-bold pt-20 p-2">Let's see what you know!</h1>
          <h2 className="text-2xl text-gray-800 font-semibold p-1">Hit the Start Recording button and summarize the topic in your own words.</h2>
          <h2 className="text-2xl text-gray-800 font-semibold p-1">When you're done, hit Results.</h2>
          <h2 className="text-2xl text-gray-800 font-semibold p-1">StegoStudy will listen to your recording and tell you what you missed.</h2>
          <div className="flex justify-center items-center gap-4 p-4">
            <button className="w-1/3 py-4 bg-red-400 text-2xl text-background rounded-md hover:bg-red-500 transition-colors"><VoiceRecorder /></button> <br />
            <Link 
              to="/results" className="w-1/3 py-4 text-2xl bg-primary text-background rounded-md hover:bg-accent transition-colors">
              <button className="">Results</button>
            </Link>
          </div>
          <p>study page with ai</p>
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

