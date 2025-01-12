import React from 'react'
import { Link } from 'react-router-dom'
import StudyCard from './studyCard'
import FileUpload from './fileupload'

export default function upload() {
  return (
    <div>
      <header className="flex fixed top-0 left-0 right-0 justify-between items-center px-8 py-4 bg-white shadow-md z-50">
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
          <h1 className="text-6xl font-bold text-primary p-4 pt-20">What are we learning today?</h1>
          <h2 className="text-3xl text-gray-800 font-semibold p-4">Choose one of our pre-made study sets</h2>
          <div className="grid grid-cols-3 gap-4 py-4">
            <Link to="/study">
            <StudyCard title="AP US History" desc="Study the history of the United States from 1492 to the present day, complete with revolutions, wars, and more!" />
            </Link>
            <Link to="/study">
            <StudyCard title="MATH137" desc="Learn the basics of calculus, including limits and derivatives!" />
            </Link>
            <Link to="/study">
            <StudyCard title="Intro to Psychology" desc="Have you ever wondered how the mind works? Learn the basics of psychology here!" />
            </Link>
          </div>
          <h2 className="text-3xl text-gray-800 font-semibold p-4">Or upload your own material!</h2>
          <FileUpload />
        </div>
      </div>
    </div>
  )
}
