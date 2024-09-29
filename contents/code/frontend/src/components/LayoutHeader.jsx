import { useState } from 'react'



const LayoutHeader = () => { 


  const [isLoggedIn, setIsLoggedIn] = useState(false)
  const [showRegister, setShowRegister] = useState(false)



  return ( 
    <header className="bg-white shadow-md p-4">
    <div className="container mx-auto flex justify-between items-center">
    <div className="flex items-center space-x-2">
    📖 BlogApp
    <span className="text-xl font-bold">BlogApp</span>
    </div>
    <div>
    {isLoggedIn ? (
    <button onClick={() => setIsLoggedIn(false)}>Logout</button>
    ) : (
    <div className="space-x-2">
    <button onClick={() => setShowRegister(false)}>Login</button>
    <button onClick={() => setShowRegister(true)}>Register</button>
    </div>
    )}
    </div>
    </div>
    </header>
  );
};

export default LayoutHeader;
