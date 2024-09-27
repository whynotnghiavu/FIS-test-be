import React, { useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";

const OtpPage = () => {
  const navigate = useNavigate();
  const location = useLocation();

  const { otp_qr_code } = location.state || {};

  const [otp, setOtp] = useState("");
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");

  const handleChange = (e) => {
    setOtp(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const accessToken = localStorage.getItem("access_token");

    try {
      const response = await fetch(
        `https://127.0.0.1:8000/api/v1/users/verify-otp?otp=${otp}`,
        {
          method: "POST",
          headers: {
            Accept: "application/json",
            Authorization: `Bearer ${accessToken}`,
          },
        }
      );

      const data = await response.json();
      if (response.ok) {
        setSuccess("OTP verified successfully!");
        setError("");

        const { access_token } = data;

        localStorage.setItem("access_token", access_token);

        navigate("/");
      } else {
        throw new Error(data.detail || "OTP verification failed");
      }
    } catch (error) {
      setError(error.message || "OTP verification failed");
      setSuccess("");
      console.error(error);
    }
  };

  return (
    <div className="container mt-5">
      {otp_qr_code && (
        <div className="text-center mt-4">
          <h2>OTP QR Code</h2>
          <img
            src={`data:image/png;base64,${otp_qr_code}`}
            alt="OTP QR Code"
            style={{ width: "150px", height: "150px" }}
          />
        </div>
      )}

      <h2>Verify OTP</h2>
      {error && <div className="alert alert-danger">{error}</div>}
      {success && <div className="alert alert-success">{success}</div>}
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label>Enter OTP</label>
          <input
            type="text"
            className="form-control"
            value={otp}
            onChange={handleChange}
            required
          />
        </div>
        <button type="submit" className="btn btn-primary">
          Verify OTP
        </button>
      </form>
    </div>
  );
};

export default OtpPage;
