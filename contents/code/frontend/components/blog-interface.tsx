'use client'

import { useState } from 'react'
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Textarea } from "@/components/ui/textarea"
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar"
import { BookOpen, MessageSquare, User } from 'lucide-react'

// Mock data
const categories = ['Technology', 'Science', 'Health', 'Entertainment', 'Sports']
const posts = [
  { id: 1, title: 'First Post', content: 'This is the content of the first post.', author: 'John Doe', comments: [
    { id: 1, author: 'Jane Smith', content: 'Great post!' },
    { id: 2, author: 'Bob Johnson', content: 'I agree with Jane.' }
  ]},
  { id: 2, title: 'Second Post', content: 'This is the content of the second post.', author: 'Jane Smith', comments: [
    { id: 3, author: 'John Doe', content: 'Interesting perspective.' }
  ]},
]





export function Header() {
return (
  <h1>Hello</h1>
)
}






export function BlogInterfaceComponent() {
  const [isLoggedIn, setIsLoggedIn] = useState(false)
  const [showRegister, setShowRegister] = useState(false)

  return (
    <div className="min-h-screen bg-gray-100">
<Header/>
{/* Header */}
      <header className="bg-white shadow-md p-4">
        <div className="container mx-auto flex justify-between items-center">
          <div className="flex items-center space-x-2">
            <BookOpen className="h-8 w-8 text-blue-500" />
            <span className="text-xl font-bold">BlogApp</span>
          </div>
          <div>
            {isLoggedIn ? (
              <Button onClick={() => setIsLoggedIn(false)}>Logout</Button>
            ) : (
              <div className="space-x-2">
                <Button onClick={() => setShowRegister(false)}>Login</Button>
                <Button onClick={() => setShowRegister(true)}>Register</Button>
              </div>
            )}
          </div>
        </div>
      </header>

      <div className="container mx-auto mt-8 flex">
        {/* Sidebar with categories */}
        <aside className="w-1/4 pr-8">
          <h2 className="text-xl font-bold mb-4">Categories</h2>
          <ul>
            {categories.map((category, index) => (
              <li key={index} className="mb-2">
                <a href="1111111111" className="text-blue-500 hover:underline">{category}</a>
              </li>
            ))}
          </ul>
        </aside>

        {/* Main content */}
        <main className="w-3/4">
          {/* Login/Register form */}
          {!isLoggedIn && (
            <div className="bg-white p-6 rounded-lg shadow-md mb-8">
              <h2 className="text-xl font-bold mb-4">{showRegister ? 'Register' : 'Login'}</h2>
              <form className="space-y-4">
                <Input type="email" placeholder="Email" />
                <Input type="password" placeholder="Password" />
                {showRegister && <Input type="password" placeholder="Confirm Password" />}
                <Button onClick={() => setIsLoggedIn(true)}>{showRegister ? 'Register' : 'Login'}</Button>
              </form>
            </div>
          )}

          {/* Posts */}
          {posts.map(post => (
            <div key={post.id} className="bg-white p-6 rounded-lg shadow-md mb-8">
              <h2 className="text-2xl font-bold mb-4">{post.title}</h2>
              <p className="mb-4">{post.content}</p>
              <p className="text-sm text-gray-500 mb-4">Posted by {post.author}</p>

              {/* Comments */}
              <div className="mt-6">
                <h3 className="text-lg font-semibold mb-4">Comments</h3>
                {post.comments.map(comment => (
                  <div key={comment.id} className="flex items-start space-x-4 mb-4">
                    <Avatar>
                      <AvatarImage src={`https://api.dicebear.com/6.x/initials/svg?seed=${comment.author}`} />
                      <AvatarFallback><User /></AvatarFallback>
                    </Avatar>
                    <div>
                      <p className="font-semibold">{comment.author}</p>
                      <p>{comment.content}</p>
                    </div>
                  </div>
                ))}
              </div>

              {/* Add comment form */}
              {isLoggedIn && (
                <form className="mt-6">
                  <Textarea placeholder="Add a comment..." className="mb-2" />
                  <Button>Post Comment</Button>
                </form>
              )}
            </div>
          ))}
        </main>
      </div>
    </div>
  )
}