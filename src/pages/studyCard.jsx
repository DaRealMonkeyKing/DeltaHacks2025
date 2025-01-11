import React from 'react'

export default function studyCard(props) {
    const {title, desc} = props
  return (
    <div
  className="max-w-xs min-h-72 overflow-hidden bg-white border border-gray-200 rounded-xl shadow-md transform transition-all duration-500 hover:shadow-lg hover:scale-105 relative group">
  <div
    className="absolute inset-0 bg-gradient-to-br from-gray-100 to-white opacity-0 transition-opacity duration-500 group-hover:opacity-30 blur-md">
  </div>
  <div className="p-6 relative z-10">
    <p class="text-xl font-semibold text-gray-800">{title}</p>
    <p class="mt-2 text-gray-600">
      {desc}
    </p>
  </div>
</div>

  )
}