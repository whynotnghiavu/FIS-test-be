import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

const LoginPage = () => {
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    email: "",
    password: "",
  });

  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const urlencodedData = new URLSearchParams();
    urlencodedData.append("grant_type", "password");
    urlencodedData.append("username", formData.email);
    urlencodedData.append("password", formData.password);
    urlencodedData.append("scope", "");
    urlencodedData.append("client_id", "string");
    urlencodedData.append("client_secret", "string");

    try {
      const response = await fetch(
        "https://127.0.0.1:8000/api/v1/users/login",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/x-www-form-urlencoded",
            Accept: "application/json",
          },
          body: urlencodedData.toString(),
        }
      );

      const data = await response.json();
      if (response.ok) {
        const { access_token, otp_qr_code } = data;
        setSuccess("Logged in successfully!");
        setError("");

        localStorage.setItem("access_token", access_token);

        if (otp_qr_code) {
          navigate("/otp", { state: { otp_qr_code } });
        } else {
          navigate("/");
        }
      } else {
        throw new Error(data.detail || "Login failed");
      }
    } catch (error) {
      setError(error.message || "Login failed");
      setSuccess("");
      console.error(error);
    }
  };

  return (
    <div className="container mt-5">
      <h2>Login</h2>
      {error && <div className="alert alert-danger">{error}</div>}
      {success && <div className="alert alert-success">{success}</div>}
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label>Email address</label>
          <input
            type="email"
            className="form-control"
            name="email"
            value={formData.email}
            onChange={handleChange}
            required
          />
        </div>

        <div className="form-group">
          <label>Password</label>
          <input
            type="password"
            className="form-control"
            name="password"
            value={formData.password}
            onChange={handleChange}
            required
          />
        </div>

        <button type="submit" className="btn btn-primary">
          Login
        </button>
      </form>
    </div>
  );
};

export default LoginPage;
