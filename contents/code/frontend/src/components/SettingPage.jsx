import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

const SettingPage = () => {
  const navigate = useNavigate();
  const [otpCode, setOtpCode] = useState("");
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(false);

  const handleGetOtp = async () => {
    setLoading(true);
    setMessage("");
    const accessToken = localStorage.getItem("access_token");
    try {
      const response = await fetch(
        "https://127.0.0.1:8000/api/v1/users/save-recovery-otp",
        {
          method: "GET",
          headers: {
            accept: "application/json",
            Authorization: `Bearer ${accessToken}`,
          },
        }
      );
      const data = await response.json();
      if (response.ok) {
        setMessage(JSON.stringify(data));
        console.log(data);
      } else {
        throw new Error(data.detail || "An error occurred.");
      }
    } catch (error) {
      setMessage(`Error: ${error.message}`);
    } finally {
      setLoading(false);
    }
  };

  const handleVerifyOtp = async () => {
    setLoading(true);
    setMessage("");
    const accessToken = localStorage.getItem("access_token");
    try {
      const response = await fetch(
        `https://127.0.0.1:8000/api/v1/users/verify-recovery-otp?code=${otpCode}`,
        {
          method: "POST",
          headers: {
            accept: "application/json",
            Authorization: `Bearer ${accessToken}`,
          },
        }
      );
      const data = await response.json();
      if (response.ok) {
        setMessage("OTP code verified successfully!");

        console.log(data);
        const { otp_qr_code } = data;
        navigate("/otp", { state: { otp_qr_code } });
      } else {
        throw new Error(data.detail || "Invalid OTP code");
      }
    } catch (error) {
      setMessage(`Error: ${error.message}`);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container mt-5">
      <div className="mb-3">
        <button
          className="btn btn-primary"
          onClick={handleGetOtp}
          disabled={loading}
        >
          <svg
            class="icon download-icon"
            xmlns="http://www.w3.org/2000/svg"
            width="24"
            height="24"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
          >
            <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
            <polyline points="7 10 12 15 17 10"></polyline>
            <line x1="12" x2="12" y1="15" y2="3"></line>
          </svg>

          {loading ? "Download OTP code..." : "Download OTP code"}
        </button>
      </div>

      <div className="mb-3">
        <input
          type="text"
          value={otpCode}
          onChange={(e) => setOtpCode(e.target.value)}
          placeholder="Enter recovery OTP code"
          className="form-control"
        />
        <button
          className="btn btn-success mt-2"
          onClick={handleVerifyOtp}
          disabled={loading || !otpCode}
        >
          {loading ? "Verifying OTP..." : "Verify OTP code"}
        </button>
      </div>

      {message && <div className="alert alert-info">{message}</div>}
    </div>
  );
};

export default SettingPage;
