import React, { useState } from "react";
import { useNavigate } from "react-router-dom"; // Dùng để điều hướng

const SettingPage = () => {
  const navigate = useNavigate(); // Hook điều hướng
  const [otpCode, setOtpCode] = useState('');
  const [message, setMessage] = useState('');
  const [loading, setLoading] = useState(false);

  // Hàm để lấy mã OTP
  const handleGetOtp = async () => {
    setLoading(true);
    setMessage('');
    const accessToken = localStorage.getItem('access_token'); // Lấy access_token từ localStorage
    try {
      const response = await fetch('https://127.0.0.1:8000/api/v1/users/save-recovery-otp', {
        method: 'GET',
        headers: {
          'accept': 'application/json',
          'Authorization': `Bearer ${accessToken}` // Sử dụng access_token trong header
        }
      });
      const data = await response.json();
      if (response.ok) {
        setMessage(JSON.stringify(data));
        console.log(data);
      } else {
        throw new Error(data.detail || 'Không thể lấy mã OTP');
      }
    } catch (error) {
      setMessage(`Lỗi: ${error.message}`);
    } finally {
      setLoading(false);
    }
  };

  // Hàm để xác minh mã OTP
  const handleVerifyOtp = async () => {
    setLoading(true);
    setMessage('');
    const accessToken = localStorage.getItem('access_token'); // Lấy access_token từ localStorage
    try {
      const response = await fetch(`https://127.0.0.1:8000/api/v1/users/verify-recovery-otp?code=${otpCode}`, {
        method: 'POST',
        headers: {
          'accept': 'application/json',
          'Authorization': `Bearer ${accessToken}` // Sử dụng access_token trong header
        }
      });
      const data = await response.json();
      if (response.ok) {
        setMessage('Mã OTP xác minh thành công!');



        console.log(data);
        const {   otp_qr_code } = data;
        navigate("/otp", { state: { otp_qr_code } });

      } else {
        throw new Error(data.detail || 'Mã OTP không hợp lệ');
      }
    } catch (error) {
      setMessage(`Lỗi: ${error.message}`);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container mt-5">
      <h2>Setting</h2>

      <div className="mb-3">
        <button className="btn btn-primary" onClick={handleGetOtp} disabled={loading}>
          {loading ? 'Đang gửi mã OTP...' : 'Gửi mã OTP'}
        </button>
      </div>

      <div className="mb-3">
        <input 
          type="text" 
          value={otpCode} 
          onChange={(e) => setOtpCode(e.target.value)} 
          placeholder="Nhập mã OTP" 
          className="form-control"
        />
        <button className="btn btn-success mt-2" onClick={handleVerifyOtp} disabled={loading || !otpCode}>
          {loading ? 'Đang xác minh...' : 'Xác minh mã OTP'}
        </button>
      </div>

      {message && <div className="alert alert-info">{message}</div>}
    </div>
  );
};

export default SettingPage;
