let mediaRecorder;
let audioChunks = [];
let audioBlob;
let audioUrl;
let audioPlayer = document.getElementById('audioPlayer');
let audioUpload = document.getElementById('audioUpload');
let audioFilePath = ''; // Track the uploaded/recorded audio file path

// Start recording audio
async function startRecording() {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });

    mediaRecorder = new MediaRecorder(stream, { mimeType: 'audio/webm' });
    audioChunks = [];

    mediaRecorder.ondataavailable = (event) => {
        audioChunks.push(event.data);
    };

    mediaRecorder.onstop = async () => {
        const webmBlob = new Blob(audioChunks, { type: 'audio/webm' });
        const wavBlob = await convertToWav(webmBlob);
    
        audioUrl = URL.createObjectURL(wavBlob);
        audioPlayer.src = audioUrl;
    
        // Save the recorded file locally and send to the server
        const formData = new FormData();
        formData.append('audioFile', wavBlob, 'recorded_audio.wav');
    
        try {
            const response = await fetch('/save_file', { 
                method: 'POST',
                body: formData,
            });

            if (response.ok) {
                console.log('File saved successfully!');
                audioFilePath = URL.createObjectURL(wavBlob); // Store the path of the recorded audio
            } else {
                console.error('Failed to save the file.');
            }
        } catch (error) {
            console.error('Error while saving the file:', error);
        }
    };

    mediaRecorder.start();
}

// Stop recording audio
function stopRecording() {
    if (mediaRecorder && mediaRecorder.state === 'recording') {
        mediaRecorder.stop();
    }
}

// Trigger the file upload input
function triggerUpload() {
    audioUpload.click();
}

// Handle file upload
function handleFileUpload(event) {
    const file = event.target.files[0];
    if (file && (file.type === 'audio/wav' || file.type === 'audio/mp3')) {
        const fileURL = URL.createObjectURL(file);
        audioPlayer.src = fileURL;
        audioFilePath = fileURL; // Store the uploaded audio path
    } else {
        alert('Please upload a valid .wav or .mp3 audio file.');
    }
}

// Process the audio

async function processAudio() {
    if (!audioFilePath) {
        alert('No audio file selected or recorded!');
        return;
    }

    try {
        const response = await fetch('/process_audio', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ filePath: audioFilePath }),
        });

        const data = await response.json();
        if (response.ok) {
            alert('Processing complete: ' + data.transcription);
            console.log(data.transcription);
        } else {
            alert('Processing failed: ' + data.error);
            console.error(data.error);
        }
    } catch (error) {
        console.error('Error processing audio:', error);
    }
}

document.getElementById('processButton').addEventListener('click', processAudio);



// Utility function to convert WebM data to WAV
async function convertToWav(webmBlob) {
    const audioBuffer = await blobToAudioBuffer(webmBlob);
    return audioBufferToWav(audioBuffer);
}

// Convert Blob to AudioBuffer
async function blobToAudioBuffer(blob) {
    const arrayBuffer = await blob.arrayBuffer();
    const audioContext = new (window.AudioContext || window.webkitAudioContext)();
    return await audioContext.decodeAudioData(arrayBuffer);
}

// Convert AudioBuffer to WAV Blob
function audioBufferToWav(audioBuffer) {
    const numOfChannels = audioBuffer.numberOfChannels;
    const sampleRate = audioBuffer.sampleRate;
    const format = 1; // PCM
    const bitDepth = 16;

    let result;
    const bytesPerSample = bitDepth / 8;
    const blockAlign = numOfChannels * bytesPerSample;

    const bufferLength = audioBuffer.length * numOfChannels * bytesPerSample;
    const wavBuffer = new ArrayBuffer(44 + bufferLength);
    const view = new DataView(wavBuffer);

    
    writeString(view, 0, 'RIFF');
    
    view.setUint32(4, 36 + bufferLength, true);
    
    writeString(view, 8, 'WAVE');
    
    writeString(view, 12, 'fmt ');
    
    view.setUint32(16, 16, true);
    
    view.setUint16(20, format, true);
    
    view.setUint16(22, numOfChannels, true);
    
    view.setUint32(24, sampleRate, true);
    
    view.setUint32(28, sampleRate * blockAlign, true);
    
    view.setUint16(32, blockAlign, true);
    
    view.setUint16(34, bitDepth, true);
    
    writeString(view, 36, 'data');
    
    view.setUint32(40, bufferLength, true);

    
    let offset = 44;
    for (let i = 0; i < audioBuffer.length; i++) {
        for (let channel = 0; channel < numOfChannels; channel++) {
            const sample = audioBuffer.getChannelData(channel)[i];
            const intSample = sample < 0 ? sample * 32768 : sample * 32767; 
            view.setInt16(offset, intSample, true);
            offset += 2;
        }
    }

    return new Blob([view], { type: 'audio/wav' });
}

function writeString(view, offset, string) {
    for (let i = 0; i < string.length; i++) {
        view.setUint8(offset + i, string.charCodeAt(i));
    }
}
