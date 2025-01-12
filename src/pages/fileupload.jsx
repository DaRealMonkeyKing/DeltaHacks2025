import React, { useState } from 'react'

export default function FileUpload() {
  const [file, setFile] = useState(null)
  const [message, setMessage] = useState('')

  const handleFileChange = async (e) => {
    const selectedFile = e.target.files[0]
    if (selectedFile && selectedFile.type === 'application/pdf') {
      setFile(selectedFile)
      
      const formData = new FormData()
      formData.append('file', selectedFile)

      try {
        const response = await fetch('http://127.0.0.1:5000/upload', {
          method: 'POST',
          body: formData,
        })

        const data = await response.json()
        if (response.ok) {
          setMessage('File uploaded successfully!')
          console.log('Success:', data)
        } else {
          setMessage('Upload failed')
          console.error('Error:', data)
        }
      } catch (error) {
        setMessage('Error uploading file')
        console.error('Error:', error)
      }
    } else {
      setMessage('Please select a PDF file')
    }
  }

  return (
    <div>
      <div className="max-w-md mx-auto rounded-lg overflow-hidden md:max-w-xl">
        <div className="md:flex">
          <div className="w-full p-3">
            <div className="relative h-48 rounded-lg border-2 border-primary bg-gray-50 flex justify-center items-center shadow-lg hover:shadow-xl transition-shadow duration-300 ease-in-out">
              <div className="absolute flex flex-col items-center">
                <img
                  alt="File Icon"
                  className="mb-3"
                  src="https://img.icons8.com/dusk/64/000000/file.png"
                />
                <span className="block text-gray-500 font-semibold">
                  Drag & drop your PDF here
                </span>
                <span className="block text-gray-400 font-normal mt-1">
                  or click to upload
                </span>
                {file && (
                  <span className="text-primary mt-2">
                    Selected: {file.name}
                  </span>
                )}
                {message && (
                  <span className={`mt-2 ${message.includes('Error') ? 'text-red-500' : 'text-green-500'}`}>
                    {message}
                  </span>
                )}
              </div>

              <input
                accept=".pdf"
                className="h-full w-full opacity-0 cursor-pointer"
                type="file"
                onChange={handleFileChange}
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
