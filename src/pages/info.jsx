import React from 'react'
import { Link } from 'react-router-dom'

export default function Info() {
  return (
    <div>
      <div className="min-h-screen">
        <div className="flex justify-center min-h-1/3 pt-20 pb-10">
            <div className="text-center max-w-3xl">
                <h1 className="text-6xl font-bold text-primary">What is StegoStudy?</h1>
                <p className="text-2xl text-gray-800 font-semibold pt-4">Dinosaur by day, study pal by night, StegoStudy is the tool you need to achieve all your learning goals. </p>
            </div>
            </div>
            <div className="grid grid-cols-3 gap-4 max-w-7xl mx-auto">
                <div className=" flex-col justify-center shadow-md rounded-xl hover:shadow-lg hover:scale-105 p-4 transition-transform duration-500">
                    <h2 className="text-3xl font-bold text-primary">How StegoStudy works</h2>
                    <p className="text-xl text-gray-800 p-4">Inspired by the Feynman Technique, StegoStudy uses AI to pick out the most important topics from a given PDF. Record yourself explaining the content of the PDF and upload it to the app. StegoStudy will then use AI to grade your performance and provide you with a score. </p>
                </div>
                <div className="flex-col justify-center shadow-md rounded-xl hover:shadow-lg hover:scale-105 p-4 transition-transform duration-500">
                    <h2 className="text-3xl font-bold text-primary">What is the Feynman Technique?</h2>
                    <p className="text-xl text-gray-800 p-4">The Feynman Technique, StegoStudy's favorite study method, is a way to learn by teaching. It involves explaining the content of a topic to someone else and having them point out the gaps in your knowledge. Studies show that this method is one of the most effective ways to learn! </p>
                </div>
                <div className=" flex-col justify-center shadow-md rounded-xl hover:shadow-lg hover:scale-105 p-4 transition-transform duration-500">
                    <h2 className="text-3xl font-bold text-primary">Who is StegoStudy for?</h2>
                    <p className="text-xl text-gray-800 p-4">While StegoStudy can be used by just about anyone wishing to learn, the goal of StegoStudy is to be a free and accessible tool for students of all ages, allowing them to achieve all their learning goals.</p>
                </div>
            </div>
        </div>
      </div>
  )
}
