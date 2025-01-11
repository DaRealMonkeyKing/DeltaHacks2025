import React from 'react'
import { Link } from 'react-router-dom'

export default function results() {
  return (
    <div>
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
  )
}
