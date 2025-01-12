import React from 'react'
import Hero from './hero'
import Info from './info'
import { Link } from 'react-router-dom'

export default function Home() {
  return (
    <div>
      <div className="bg-primary">
        <Hero />
      </div>
      <Info />
    </div>
  )
}
