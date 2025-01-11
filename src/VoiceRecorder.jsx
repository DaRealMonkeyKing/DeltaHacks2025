import React, { useState } from "react";
import axios from "axios";

const VoiceRecorder = () => {
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
                        "http://127.0.0.1:5000/upload",
                        formData,
                        {
                            headers: { "Content-Type": "multipart/form-data" },
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

    const fetchTranscription = async () => {
        try {
            const response = await axios.get(
                "http://127.0.0.1:5000/transcribe"
            );

            setTranscription(response.data.transcription);
            console.log(response.data.transcription);
        } catch (err) {
            console.error(err);
        }
    };

    return (
        <div>
            <button
                className="bg-red-400 text-black rounded-md px-10 py-2"
                onClick={recording ? stopRecording : startRecording}
            >
                {recording ? "Stop Recording" : "Start Recording"}
            </button>
            {audioUrl && <audio controls src={audioUrl} />}
            {transcription && <p>Transcription: {transcription}</p>}
        </div>
    );
};

export default VoiceRecorder;
