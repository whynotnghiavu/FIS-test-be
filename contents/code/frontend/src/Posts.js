import React, { useEffect, useState } from 'react';

const Posts = () => {
  const [posts, setPosts] = useState([]);

  // Fetch posts when the component mounts
  useEffect(() => {
    fetch('https://127.0.0.1:8080/api/v1/posts?skip=0&limit=100', {
      headers: {
        'accept': 'application/json',
      },
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then((data) => {
        setPosts(data); // Save the data to state
      })
      .catch((error) => {
        console.error('Error fetching posts:', error);
      });
  }, []);

  return (
    <div className="container">
      <div className="row">
        <div className="col-sm-4">
          <ul className="nav nav-pills flex-column">
            {posts.map((post) => (
              <li className="nav-item" key={post.id}>
                {/* <a className="nav-link" href="/"> */}
                





<h2 class="text-2xl font-bold mb-4">  {post.id}</h2>
<h2 class="text-2xl font-bold mb-4">  {post.title}</h2>
<p class="mb-4">   {post.content}</p>
<p class="text-sm text-gray-500 mb-4">Posted by user id:   {post.created_at}</p>
<p class="text-sm text-gray-500 mb-4">Posted by user id:   {post.user_id}</p>
<p class="text-sm text-gray-500 mb-4">Posted by user id:   {post.category_id}</p>

{/* Thông tin */}
{/* Thông tin */}
{/* Thông tin */}
{/* Thông tin */}
{/* Thông tin */}
{/* Thông tin */}
{/* Thông tin */}
{/* Thông tin */}


                {/* </a> */}
              </li>
            ))}
          </ul>
        </div>
      </div>
    </div>
  );
};

export default Posts;
