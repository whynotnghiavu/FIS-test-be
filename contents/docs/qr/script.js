// Generate the QR Code
document.addEventListener('DOMContentLoaded', function () {
    const qrValue = "otpauth://totp/Example:alice@google.com?secret=JBSWY3DPEHPK3PXP&issuer=Example";
    const qrCanvas = document.getElementById('qrcode');
    
    const qrCode = new QRCode(qrCanvas, {
        text: qrValue,
        width: 200,
        height: 200,
        colorDark: "#000000",
        colorLight: "#ffffff",
    });

    const otpForm = document.getElementById('otpForm');
    const otpInput = document.getElementById('otpInput');
    const verificationMessage = document.getElementById('verificationMessage');

    // Handle OTP submission
    otpForm.addEventListener('submit', function (e) {
        e.preventDefault();
        const otp = otpInput.value.trim();
        
        // Simulate verification (for demo purposes, any OTP is "verified")
        if (otp) {
            verificationMessage.classList.remove('hidden');
        }
    });
});
