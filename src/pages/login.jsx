import React from 'react'
import { Link } from 'react-router-dom'

export default function Login() {
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
        <div class="w-96 rounded-lg shadow h-auto p-6 bg-white relative overflow-hidden">
          <div class="flex flex-col justify-center items-center space-y-2">
            <h2 class="text-3xl font-bold text-primary">Login</h2>
            <p class="text-gray-800">Enter details below.</p>
          </div>
          <form class="w-full mt-4 space-y-3">
            <div>
              <input
                class="outline-none border-2 rounded-md px-2 py-1 text-slate-500 w-full focus:border-blue-300"
                placeholder="Username"
                id="username"
                name="username"
                type="text"
              />
            </div>
            <div>
              <input
                class="outline-none border-2 rounded-md px-2 py-1 text-slate-500 w-full focus:border-blue-300"
                placeholder="Password"
                id="password"
                name="password"
                type="password"
              />
            </div>
            <div class="flex items-center justify-between">
              <div class="flex items-center">
                <input
                  class="mr-2 w-4 h-4"
                  id="remember"
                  name="remember"
                  type="checkbox"
                />
                <span class="text-gray-800">Remember me </span>
              </div>
              <a class="text-primary font-medium hover:underline" href="#"
                >Forgot Password</a
              >
            </div>
            <Link to="/upload">
            <button
              class="w-full justify-center py-1 bg-primary hover:bg-accent active:bg-accent rounded-md text-white ring-2"
              type="submit"
            >
              Log in
            </button>
            </Link>
            <p class="flex justify-center space-x-1">
              <span class="text-gray-800"> First time here? </span>
              <a class="text-primary hover:underline" href="#">Sign Up</a>
            </p>
          </form>
        </div>
        </div>
      </div>
    </div>
  )
}
