document.addEventListener('DOMContentLoaded', () => {
    const socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
    const video = document.getElementById('video');
    const statusBox = document.getElementById('status-box');

    // Handle connection success
    socket.on('connect', () => {
        console.log('Connected to server!');
        updateStatus('Camera starting...', 'info');
    });

    // Get camera access
    if (navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({ video: true })
            .then(stream => {
                video.srcObject = stream;
                updateStatus('Scanning for faces...', 'info');
                // Send frames to the server every 2 seconds
                setInterval(() => {
                    sendFrame(video);
                }, 2000);
            })
            .catch(err => {
                console.error("Error accessing camera: ", err);
                updateStatus('Camera access denied!', 'error');
            });
    }

    function sendFrame(videoElement) {
        const canvas = document.createElement('canvas');
        canvas.width = videoElement.videoWidth;
        canvas.height = videoElement.videoHeight;
        const context = canvas.getContext('2d');
        context.drawImage(videoElement, 0, 0, canvas.width, canvas.height);
        const data = canvas.toDataURL('image/jpeg', 0.8);
        socket.emit('image', data);
    }
    
    // Listen for responses from the server
    socket.on('response', (data) => {
        console.log('Server response:', data);
        let message = '';
        let statusType = 'info';

        switch (data.status) {
            case 'Attendance Marked!':
                message = `${data.status}<br>${data.name} (${data.id})`;
                statusType = 'success';
                break;
            case 'Already Marked Today':
                message = `${data.status}<br>${data.name} (${data.id})`;
                statusType = 'warning';
                break;
            case 'Unknown Face Detected':
                message = 'Unknown Face Detected. Please register.';
                statusType = 'error';
                break;
            default:
                message = 'Scanning for faces...';
                statusType = 'info';
        }
        updateStatus(message, statusType);
    });

    function updateStatus(message, type) {
        statusBox.innerHTML = message;
        statusBox.className = 'status-box'; // Reset classes
        if (type === 'success') statusBox.classList.add('status-success');
        else if (type === 'warning') statusBox.classList.add('status-warning');
        else if (type === 'error') statusBox.classList.add('status-error');
        else statusBox.classList.add('status-info');
    }
});