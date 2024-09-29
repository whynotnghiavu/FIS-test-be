"use client"

import { useState } from 'react'
import QRCode from 'react-qr-code'
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card"

export function QrOtpAuth() {
  const [otp, setOtp] = useState('')
  const [isVerified, setIsVerified] = useState(false)

  const qrValue = "otpauth://totp/Example:alice@google.com?secret=JBSWY3DPEHPK3PXP&issuer=Example"

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()

    if (otp !== '123456') {
      // alert('Invalid OTP')
      // return

      setIsVerified(false)
    }else{
      // alert('OTP verified successfully!')
      
      setIsVerified(true)
    }
  }

  return (
    <Card className="w-full max-w-md mx-auto">
      <CardHeader>
        <CardTitle>QR Code Authentication</CardTitle>
        <CardDescription>Scan the QR code and enter the OTP to authenticate</CardDescription>
      </CardHeader>
      <CardContent className="flex flex-col items-center space-y-6">
        <div className="bg-white p-4 rounded-lg">
          <QRCode value={qrValue} size={200} />
        </div>
        <form onSubmit={handleSubmit} className="w-full space-y-4">
          <Input
            type="text"
            placeholder="Enter OTP"
            value={otp}
            onChange={(e) => setOtp(e.target.value)}
            className="w-full"
          />
          <Button type="submit" className="w-full">
            Verify OTP
          </Button>
        </form>
      </CardContent>
      <CardFooter>
        {isVerified && (
          <p className="text-green-600 font-semibold w-full text-center">OTP verified successfully!</p>
        )}

        {!isVerified && (
          <p className="text-red-600 font-semibold w-full text-center">Invalid OTP</p>
        )}
      </CardFooter>
    </Card>
  )
}