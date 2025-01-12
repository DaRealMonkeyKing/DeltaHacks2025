import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';

export default function Results() {
  const [loading, setLoading] = useState(true);
  const [results, setResults] = useState(null);
  const transcription = localStorage.getItem('transcription');
  const file = localStorage.getItem('file');

  useEffect(() => {
    const pdfFileName = localStorage.getItem('pdfFileName');
    const transcription = localStorage.getItem('transcription');
    
    console.log("Data from localStorage:", { 
      pdfFileName, 
      transcription 
    });  // Debug log
    
    if (!transcription || !pdfFileName) {
      console.error("Missing data:", { transcription, pdfFileName });
      setLoading(false);
      return;
    }

    axios.post("http://localhost:5000/api/receive_string", { 
      transcription,
      pdfFileName
    }, {
      headers: {
        'Content-Type': 'application/json'
      }
    })
      .then((response) => {
        if (!response.data) {
          throw new Error('No data received from server');
        }
        console.log("Full response data:", response.data);
        console.log("Clusters:", response.data.cluster_results);
        console.log("Coverage:", response.data.coverage_percentage);
        setResults(response.data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error details:", {
          message: error.message,
          response: error.response?.data,
          status: error.response?.status
        });
        setLoading(false);
      });
  }, []); // Empty dependency array is fine if we only want to run once

  return (
    <div>
      <header className="flex fixed top-0 left-0 right-0 justify-between items-center px-8 py-4 bg-white shadow-md">
        <div className="h-10">
          <Link to="/">
            <img 
              src="src/assets/logo.png" 
              alt="Logo" 
              className="h-full w-auto"
            />
          </Link>
        </div>
      </header>
      <div className="flex items-center justify-center min-h-screen">
        <div className="text-center">
          <h1 className="text-6xl font-bold text-primary pt-20">Let's see how you did!</h1>
          <div className="flex items-center justify-center">
            <img src="src/assets/pizza.png" alt="Mascot" className="w-2/3" />
          </div>
          {loading ? (
            <p>Analyzing your response...</p>
          ) : results ? (
            <>
              <h2 className="text-3xl text-gray-800 font-semibold p-2">
                StegoStudy heard {Math.round(results.coverage_percentage)}% of key information in the study set.
              </h2>
              {/*<h2 className="text-3xl text-gray-800 font-semibold p-2">Here's what you missed:</h2>
              <div className="p-4">
                {Object.entries(results.cluster_results).map(([id, cluster]) => (
                  !cluster.covered && (
                    <div key={id} className="mb-4 p-4 bg-gray-100 rounded">
                      <p className="text-left">{cluster.sentences.join(' ')}</p>
                    </div>
                  )
                ))}
              </div>*/}
            </>
          ) : (
            <p>Error analyzing response</p>
          )}
          <h2 className="text-3xl text-gray-800 font-semibold p-4">Study again?</h2>
          <div className="flex justify-center items-center gap-4 pt-2 pb-10">
            <Link to="/study">
              <button className="w-[300px] py-4 bg-primary text-2xl text-background rounded-md hover:accent transition-colors">
                Try Again
              </button>
            </Link>
            <Link to="/upload">
              <button className="w-[300px] py-4 bg-primary text-2xl text-background rounded-md hover:accent transition-colors">
                New Topic
              </button>
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}
