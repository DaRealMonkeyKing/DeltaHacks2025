import React from 'react'
import { Link } from 'react-router-dom'

export default function upload() {
  return (
    <div>
        <p>Upload/choose a study set page</p>
        <Link 
          to="/study" 
          className="px-6 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 transition-colors"
        >
          study
        </Link>
    </div>
  )
}
