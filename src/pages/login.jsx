import React from 'react'
import { Link } from 'react-router-dom'

export default function Login() {
  return (
    <div>
        <p>Login page</p>
        <p>just hard code two text boxes and a button</p>
        <Link 
          to="/upload" 
          className="px-6 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 transition-colors"
        >
          Login
        </Link>
    </div>
  )
}
