// document.addEventListener('DOMContentLoaded', function({
//     // untuk mengecek mendukung getUser Media
//     if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia)
//     // Mengakses webcam untuk stream 1 
//         navigator.mediaDevices.getUserMedia({ video: true })
//             .then(function(stream){
//                 var videoElement = document.getElementById('webcamStream1');
//                 videoElement.src0object = stream;
//             })
//             .catch(function(error){
//                 console.error('Error Accessing Webcam Stream 1', error);
//             });
//     // Mengakses webcam untuk stream 2 
//     navigator.mediaDevices.getUserMedia({ video: true })
//     .then(function(stream){
//         var videoElement = document.getElementById('webcamStream2');
//         videoElement.src0object = stream;
//     })
//     .catch(function(error){
//         console.error('Error Accessing Webcam Stream 1', error);
//     });
// }else {
//     alert('Browser Tidak Mendukung getUserMedia');
// }
// ));