import React, { useState } from "react";
import axios from "axios";

const VoiceRecorder = ({onTranscriptionChange}) => {
    const [recording, setRecording] = useState(false);
    const [audioUrl, setAudioUrl] = useState(null);
    const [audioFile, setAudioFile] = useState(null);
    const [mediaRecorder, setMediaRecorder] = useState(null);
    const [transcription, setTranscription] = useState("");

    // Start recording
    const startRecording = async () => {
        try {
            const stream = await navigator.mediaDevices.getUserMedia({
                audio: true,
            });
            const recorder = new MediaRecorder(stream);
            setMediaRecorder(recorder);

            const audioChunks = [];
            recorder.ondataavailable = (event) => {
                audioChunks.push(event.data);
            };

            recorder.onstop = async () => {
                const audioBlob = new Blob(audioChunks, { type: "audio/wav" });
                const audioUrl = URL.createObjectURL(audioBlob);
                setAudioUrl(audioUrl);
                setAudioFile(audioBlob);

                // Send the audio file to Flask backend for processing (no conversion needed)
                const formData = new FormData();
                formData.append("audio", audioBlob, "audio.wav");

                try {
                    const response = await axios.post(
                        "http://127.0.0.1:5000/upload_audio",
                        formData,
                        {
                            headers: { "Content-Type": "multipart/form-data",
                                "Access-Control-Allow-Origin": "*",
                             },
                             withCredentials: false,
                        }
                    );
                    console.log("WAV file received:", response.data);
                    // Set the audio file URL (from Flask response)
                    setAudioUrl(response.data.audio_url);
                } catch (error) {
                    console.error("Error sending audio to Flask:", error);
                }
            };

            recorder.start();
            setRecording(true);
        } catch (error) {
            console.error("Error accessing the microphone:", error);
        }
    };

    // Stop recording
    const stopRecording = async () => {
        if (mediaRecorder) {
            mediaRecorder.stop();
            setRecording(false);
        }
        fetchTranscription()
    };

    const handleTranscriptionResult = (result) => {
        setTranscription(result);
        onTranscriptionChange(result);
    };

    const fetchTranscription = async () => {
        try {
            console.log("Starting transcription fetch...");
            const response = await fetch("http://127.0.0.1:5000/transcribe", {
                method: 'GET',
                mode: 'cors',
                credentials: 'omit',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                    "Access-Control-Allow-Origin": "*",
                },
            });

            console.log("Response received:", response);
            const text = await response.text();  // Try getting raw text first
            console.log("Raw response:", text);

            try {
                const data = JSON.parse(text);
                if (data && data.transcription) {
                    setTranscription(data.transcription);
                    console.log("Transcription received:", data.transcription);
                    handleTranscriptionResult(data.transcription);
                } else {
                    console.error("No transcription in response:", data);
                }
            } catch (parseError) {
                console.error("Error parsing JSON:", parseError);
                console.log("Raw response was:", text);
            }

        } catch (err) {
            console.error("Error fetching transcription:", err);
            setTranscription("Error getting transcription");
        }
    };

    return (
        <div>
            <button 
                onClick={recording ? stopRecording : startRecording}
            >
                {recording ? "Stop Recording" : "Start Recording"}
            </button>
            {/* {audioUrl && <audio controls src={audioUrl} />} */}
        </div>
    );
};

export default VoiceRecorder;
